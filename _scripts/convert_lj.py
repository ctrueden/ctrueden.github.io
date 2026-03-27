#!/usr/bin/env python3
"""Convert LiveJournal HTML scrapes from the origin/lj branch into Jekyll posts.

Usage:
    python3 convert_lj.py              # Local-only (fast), lj-cut content truncated
    python3 convert_lj.py --fetch-cuts # Fetch full posts from LJ for lj-cut entries
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Missing dependency: pip install beautifulsoup4")

try:
    import html2text
except ImportError:
    sys.exit("Missing dependency: pip install html2text")


REPO_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO_ROOT / "_posts"
LJ_FILES = range(0, 150, 10)  # 0.html through 140.html
TIMEZONE = "-0600"


def git_show(path):
    """Read a file from the origin/lj branch via git."""
    result = subprocess.run(
        ["git", "show", f"origin/lj:{path}"],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        print(f"Warning: could not read {path}: {result.stderr.strip()}")
        return None
    return result.stdout


def parse_date(text):
    """Parse LJ date like 'September 11th, 2008 (04:08 pm)' into a datetime."""
    m = re.search(r'(\w+ \d+)\w{0,2}, (\d{4}) \((\d{2}:\d{2} [ap]m)\)', text)
    if not m:
        return None
    date_str = f"{m.group(1)}, {m.group(2)} {m.group(3)}"
    return datetime.strptime(date_str, "%B %d, %Y %I:%M %p")


def parse_mood(text):
    """Extract mood from aboutentry text."""
    m = re.search(r'current mood:\s*(\w+)', text)
    return m.group(1) if m else None


def parse_song(text):
    """Extract song from aboutentry text."""
    m = re.search(r'current song:\s*(.+?)(?:\n|$)', text)
    if not m:
        return None
    song = m.group(1).strip()
    # Clean up truncated radio station info
    song = re.sub(r'\s*\(\[radio\..*$', '', song)
    return song if song else None


def slugify(title, max_len=50):
    """Convert a title to a URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    if len(slug) > max_len:
        slug = slug[:max_len].rsplit('-', 1)[0]
    return slug or "untitled"


# --- Network fetching (used with --fetch-cuts) ---

def fetch_html(url):
    """Fetch a URL and return the HTML string, or None on failure."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; lj-archive-convert/1.0)',
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
        print(f"    Could not fetch {url}: {e}")
        return None


def extract_post_content(html):
    """Extract post content div from an HTML page.

    Handles both old LJ layout (div.entrytext) and new layout
    (div.aentry-post__text).
    """
    soup = BeautifulSoup(html, 'html.parser')
    # Old layout
    content = soup.find('div', class_='entrytext')
    if content and len(content.get_text(strip=True)) > 50:
        return content
    # New layout (post2017)
    content = soup.find('div', class_='aentry-post__text')
    if content and len(content.get_text(strip=True)) > 50:
        return content
    return None


def wayback_url(url):
    """Query the Wayback Machine availability API for a snapshot URL."""
    api = f"https://archive.org/wayback/available?url={url}"
    try:
        req = urllib.request.Request(api, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; lj-archive-convert/1.0)',
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        snapshots = data.get('archived_snapshots', {})
        closest = snapshots.get('closest', {})
        return closest.get('url') if closest.get('available') else None
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError):
        return None


def fetch_full_post(url):
    """Fetch the full individual post page from LJ or Wayback Machine.

    Returns the content div (BeautifulSoup Tag), or None on failure.
    """
    # Try live LJ first
    html = fetch_html(url)
    if html:
        content = extract_post_content(html)
        if content:
            return content

    # Try Wayback Machine
    wb_url = wayback_url(url)
    if wb_url:
        print(f"    Trying Wayback Machine: {wb_url}")
        html = fetch_html(wb_url)
        if html:
            content = extract_post_content(html)
            if content:
                return content

    time.sleep(1)  # Be polite
    return None


# --- HTML cleaning and conversion ---

def has_ljcut(tag):
    """Check if a BeautifulSoup tag contains lj-cut markers."""
    return bool(tag.find_all('b', attrs={'data-widget': 'ljcut'}))


def clean_html(content_div):
    """Clean entry HTML before Markdown conversion."""
    html_str = str(content_div)

    # Convert LJ user spans to plain links
    def replace_ljuser(m):
        username = m.group(1)
        return f'<a href="https://{username}.livejournal.com/">{username}</a>'
    html_str = re.sub(
        r'<span[^>]*class="[^"]*ljuser[^"]*"[^>]*data-ljuser="([^"]*)"[^>]*>.*?</span>',
        replace_ljuser, html_str, flags=re.DOTALL,
    )
    html_str = re.sub(
        r'<span[^>]*data-ljuser="([^"]*)"[^>]*class="[^"]*ljuser[^"]*"[^>]*>.*?</span>',
        replace_ljuser, html_str, flags=re.DOTALL,
    )

    # Re-parse the cleaned HTML
    soup = BeautifulSoup(html_str, 'html.parser')

    # Remove lj-cut markers (keep surrounding content)
    for cut in soup.find_all('b', attrs={'data-widget': 'ljcut'}):
        cut.decompose()

    # Remove wbr tags
    for wbr in soup.find_all('wbr'):
        wbr.decompose()

    # Remove ad/promo elements
    for cls in ['ljsale', 'ljclear']:
        for el in soup.find_all(class_=cls):
            el.decompose()

    # Handle LJ embeds (YouTube etc.)
    for iframe in soup.find_all('iframe', class_='lj_embedcontent'):
        src = iframe.get('src', '')
        yt_match = re.search(r'youtube\.com/embed/([^?&"]+)', src)
        if yt_match:
            yt_url = f"https://www.youtube.com/watch?v={yt_match.group(1)}"
            link = soup.new_tag('a', href=yt_url)
            link.string = yt_url
            iframe.replace_with(link)
        elif src:
            iframe.decompose()

    return str(soup)


def html_to_markdown(html_str):
    """Convert HTML to clean Markdown."""
    h = html2text.HTML2Text()
    h.body_width = 0  # Don't wrap lines
    h.unicode_snob = True
    h.protect_links = True
    h.wrap_links = False
    md = h.handle(html_str)
    # Clean up excessive blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def yaml_escape(s):
    """Escape a string for YAML frontmatter."""
    if not s:
        return '""'
    s_escaped = s.replace('\\', '\\\\').replace('"', '\\"')
    return '"' + s_escaped + '"'


def process_entry(entry_div, do_fetch=False):
    """Extract post data from a single <div class="entry"> element."""
    # Title and URL
    subj_link = entry_div.find('a', class_='subj-link')
    if subj_link:
        title = subj_link.get_text(strip=True)
        original_url = subj_link.get('href', '')
    else:
        title = ''
        original_url = ''

    # Date
    about = entry_div.find('div', class_='aboutentry')
    if not about:
        return None
    about_text = about.get_text()
    dt = parse_date(about_text)
    if not dt:
        print(f"  Warning: could not parse date for '{title}': {about_text[:80]}")
        return None

    # Use date-based title for untitled posts
    if not title:
        title = dt.strftime("Untitled (%B %-d, %Y)")

    # Mood and song
    mood = parse_mood(about_text)
    song = parse_song(about_text)

    # Content
    content_div = entry_div.find('div', class_='entrytext')
    if not content_div:
        return None

    # If the entry has lj-cut markers, the listing page is missing content.
    # Fetch the full individual post page instead (if enabled).
    truncated = has_ljcut(content_div)
    if truncated and do_fetch and original_url:
        print(f"    lj-cut detected, fetching full post: {original_url}")
        full_content = fetch_full_post(original_url)
        if full_content:
            content_div = full_content
            truncated = False
        else:
            print(f"    WARNING: Could not fetch full post, using truncated version")

    cleaned_html = clean_html(content_div)
    markdown = html_to_markdown(cleaned_html)

    return {
        'title': title,
        'date': dt,
        'mood': mood,
        'song': song,
        'original_url': original_url,
        'content': markdown,
        'truncated': truncated,
    }


def write_post(post):
    """Write a single post as a Jekyll Markdown file."""
    date_str = post['date'].strftime('%Y-%m-%d')
    slug = slugify(post['title'])
    filename = f"{date_str}-{slug}.md"
    filepath = POSTS_DIR / filename

    # Handle duplicate filenames
    counter = 2
    while filepath.exists():
        filename = f"{date_str}-{slug}-{counter}.md"
        filepath = POSTS_DIR / filename
        counter += 1

    # Build frontmatter
    dt_str = post['date'].strftime(f'%Y-%m-%d %H:%M:%S {TIMEZONE}')
    lines = [
        '---',
        f'title: {yaml_escape(post["title"])}',
        f'date: {dt_str}',
    ]
    if post['mood']:
        lines.append(f'mood: {post["mood"]}')
    if post['song']:
        lines.append(f'song: {yaml_escape(post["song"])}')
    if post['original_url']:
        lines.append(f'original_url: {post["original_url"]}')
    if post['truncated']:
        lines.append('truncated: true')
    lines.append('---')
    lines.append('')
    lines.append(post['content'])
    lines.append('')

    filepath.write_text('\n'.join(lines))
    return filepath


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fetch-cuts', action='store_true',
                        help='Fetch full posts from LJ for entries with lj-cut')
    args = parser.parse_args()

    POSTS_DIR.mkdir(exist_ok=True)

    total = 0
    truncated_posts = []
    for n in LJ_FILES:
        path = f"lj/{n}.html"
        print(f"Processing {path}...")
        html = git_show(path)
        if not html:
            continue

        soup = BeautifulSoup(html, 'html.parser')
        entries = soup.find_all('div', class_='entry')
        print(f"  Found {len(entries)} entries")

        for entry in entries:
            post = process_entry(entry, do_fetch=args.fetch_cuts)
            if not post:
                continue
            fp = write_post(post)
            status = " [TRUNCATED]" if post['truncated'] else ""
            print(f"  -> {fp.name}{status}")
            if post['truncated']:
                truncated_posts.append((post['title'], post['original_url']))
            total += 1

    print(f"\nDone! Converted {total} posts to {POSTS_DIR}")
    if truncated_posts:
        print(f"\n{len(truncated_posts)} posts have truncated lj-cut content:")
        for title, url in truncated_posts:
            print(f"  - {title}: {url}")
        if not args.fetch_cuts:
            print("\nRe-run with --fetch-cuts to attempt fetching full content from LJ.")


if __name__ == '__main__':
    main()
