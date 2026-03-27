#!/usr/bin/env python3
"""Convert Facebook JSON export into categorized Markdown files.

Usage:
    python3 convert_fb.py <path-to-facebook-json>

Output structure:
    _fb/posts/        - original posts (no title, or "is feeling")
    _fb/status/       - status updates
    _fb/shares/       - shared links, photos, videos, posts, etc.
    _fb/wall/         - wall posts ("wrote on")
    _fb/recommends/   - recommendations / anti-recommendations
    _fb/added/        - added photos, videos, books, life events
    _fb/groups/       - group posts ("posted in")
    _fb/via/          - "posted something via" app posts
    _fb/other/        - anything else
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FB_DIR = REPO_ROOT / "_fb"


def fix_encoding(text):
    """Fix Facebook's mojibake: UTF-8 bytes stored as latin-1 strings."""
    try:
        return text.encode('latin-1').decode('utf-8')
    except (UnicodeDecodeError, UnicodeEncodeError):
        return text


def categorize(post):
    """Return a category string based on the post's title pattern."""
    title = post.get('title', '')
    if not title:
        return 'posts'
    if 'updated his status' in title:
        return 'status'
    if 'shared a' in title or 'shared an' in title or 'shared moments' in title:
        return 'shares'
    if 'wrote on' in title:
        return 'wall'
    if 'recommends' in title or "doesn't recommend" in title:
        return 'recommends'
    if 'added' in title:
        return 'added'
    if 'is feeling' in title:
        return 'posts'
    if 'posted in' in title:
        return 'groups'
    if 'posted something via' in title:
        return 'via'
    if 'was live' in title:
        return 'shares'
    if 'created' in title:
        return 'other'
    return 'other'


def yaml_escape(s):
    """Escape a string for YAML frontmatter."""
    if not s:
        return '""'
    s = s.replace('\\', '\\\\').replace('"', '\\"')
    return '"' + s + '"'


def extract_post_text(post):
    """Extract the main post text from the data array."""
    for d in post.get('data', []):
        if 'post' in d:
            return fix_encoding(d['post'])
    return ''


def extract_attachments(post):
    """Extract attachment info (links, media) from the post."""
    links = []
    media = []
    for att in post.get('attachments', []):
        for d in att.get('data', []):
            if 'external_context' in d:
                url = d['external_context'].get('url', '')
                name = d['external_context'].get('name', '')
                source = d['external_context'].get('source', '')
                if url:
                    links.append({'url': url, 'name': fix_encoding(name), 'source': fix_encoding(source)})
            if 'media' in d:
                m = d['media']
                media.append({
                    'uri': m.get('uri', ''),
                    'description': fix_encoding(m.get('description', '')),
                })
            if 'place' in d:
                place = d['place']
                links.append({
                    'type': 'place',
                    'name': fix_encoding(place.get('name', '')),
                    'url': place.get('url', ''),
                })
    return links, media


def post_to_file(post, category, output_dir):
    """Write a single Facebook post as a Markdown file."""
    ts = post['timestamp']
    dt = datetime.fromtimestamp(ts, tz=timezone.utc).astimezone()
    date_str = dt.strftime('%Y-%m-%d')
    time_str = dt.strftime('%H%M%S')
    dt_full = dt.strftime('%Y-%m-%d %H:%M:%S %z')

    filename = f"{date_str}-{time_str}.md"
    filepath = output_dir / filename

    # Handle duplicate timestamps
    counter = 2
    while filepath.exists():
        filename = f"{date_str}-{time_str}-{counter}.md"
        filepath = output_dir / filename
        counter += 1

    # Extract fields
    title = fix_encoding(post.get('title', ''))
    text = extract_post_text(post)
    links, media = extract_attachments(post)

    # Build frontmatter
    lines = ['---']
    lines.append(f'date: {dt_full}')
    if title:
        lines.append(f'title: {yaml_escape(title)}')
    lines.append(f'category: {category}')

    if links:
        lines.append('links:')
        for link in links:
            if link.get('type') == 'place':
                lines.append(f'  - type: place')
                lines.append(f'    name: {yaml_escape(link["name"])}')
                if link.get('url'):
                    lines.append(f'    url: {yaml_escape(link["url"])}')
            else:
                lines.append(f'  - url: {yaml_escape(link["url"])}')
                if link.get('name'):
                    lines.append(f'    name: {yaml_escape(link["name"])}')
                if link.get('source'):
                    lines.append(f'    source: {yaml_escape(link["source"])}')

    if media:
        lines.append('media:')
        for m in media:
            lines.append(f'  - uri: {yaml_escape(m["uri"])}')
            if m.get('description'):
                lines.append(f'    description: {yaml_escape(m["description"])}')

    lines.append('---')
    lines.append('')

    # Body
    if text:
        lines.append(text)
        lines.append('')

    filepath.write_text('\n'.join(lines), encoding='utf-8')
    return filepath


def main():
    if len(sys.argv) < 2:
        sys.exit(f"Usage: {sys.argv[0]} <path-to-facebook-json>")

    json_path = Path(sys.argv[1])
    if not json_path.exists():
        sys.exit(f"File not found: {json_path}")

    with open(json_path, 'r') as f:
        posts = json.load(f)

    print(f"Loaded {len(posts)} posts from {json_path}")

    # Categorize and count
    from collections import Counter
    counts = Counter()
    for post in posts:
        cat = categorize(post)
        counts[cat] += 1

    print("\nCategories:")
    for cat, count in counts.most_common():
        print(f"  {cat}: {count}")

    # Create output directories
    categories = set(counts.keys())
    for cat in categories:
        (FB_DIR / cat).mkdir(parents=True, exist_ok=True)

    # Convert
    total = 0
    for post in posts:
        cat = categorize(post)
        output_dir = FB_DIR / cat
        fp = post_to_file(post, cat, output_dir)
        total += 1

    print(f"\nDone! Wrote {total} files to {FB_DIR}/")
    for cat, count in counts.most_common():
        print(f"  {FB_DIR / cat}: {count} files")


if __name__ == '__main__':
    main()
