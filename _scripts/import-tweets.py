#!/usr/bin/env python3
"""
Import tweets from Twitter export (twitter/data/tweets.js) into Jekyll _posts/.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone


TWEETS_JS = "twitter/data/tweets.js"
POSTS_DIR = "_posts"
USERNAME = "ctrueden"


def load_tweets(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip the JS variable assignment wrapper
    content = re.sub(r"^window\.YTD\.tweets\.part\d+ = ", "", content.strip())
    return json.loads(content)


def parse_date(created_at):
    # Format: "Thu Oct 31 19:16:24 +0000 2024"
    return datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")


def expand_urls(text, urls):
    """Replace t.co short URLs with their expanded versions."""
    for entry in urls:
        text = text.replace(entry["url"], entry["expanded_url"])
    return text


def replace_media_urls(text, media_list):
    """Replace t.co media URLs with markdown image syntax, or remove if no URL."""
    for media in media_list:
        url = media.get("url", "")
        img_url = media.get("media_url_https") or media.get("media_url", "")
        if url and img_url:
            if media.get("type") == "photo":
                text = text.replace(url, f"![]({img_url})")
            else:
                text = text.replace(url, img_url)
    return text


def slugify(text):
    """Convert text to a URL-friendly slug."""
    # Strip emoji and non-ASCII
    text = text.encode("ascii", "ignore").decode("ascii")
    # Lowercase
    text = text.lower()
    # Remove chars that aren't alphanumeric or spaces/hyphens
    text = re.sub(r"[^\w\s-]", "", text)
    # Replace whitespace runs with a single hyphen
    text = re.sub(r"\s+", "-", text.strip())
    # Remove leading/trailing hyphens
    text = text.strip("-")
    # Truncate
    return text[:50].rstrip("-")


def make_title(text):
    """Extract a title from tweet text (strip leading @mentions and URLs)."""
    # Strip leading @mentions
    text = re.sub(r"^(@\S+\s+)+", "", text).strip()
    # Strip markdown images
    text_for_title = re.sub(r"!\[.*?\]\(.*?\)", "", text).strip()
    # Strip URLs for title purposes
    text_for_title = re.sub(r"https?://\S+", "", text_for_title).strip()
    # Collapse extra whitespace
    text_for_title = re.sub(r"\s+", " ", text_for_title).strip()
    # Fall back to original if stripping left nothing
    if not text_for_title:
        text_for_title = re.sub(r"!\[.*?\]\(.*?\)", "", text).strip()
    if not text_for_title:
        text_for_title = text.strip()
    # Use first line or first 80 chars
    first_line = text_for_title.split("\n")[0].strip()
    if len(first_line) <= 80:
        return first_line
    # Truncate at word boundary
    truncated = first_line[:77]
    last_space = truncated.rfind(" ")
    if last_space > 40:
        truncated = truncated[:last_space]
    return truncated + "..."


def unique_path(posts_dir, date_str, slug, existing):
    base = f"{date_str}-{slug}"
    path = os.path.join(posts_dir, f"{base}.md")
    if path not in existing:
        return path
    i = 2
    while True:
        path = os.path.join(posts_dir, f"{base}-{i}.md")
        if path not in existing:
            return path
        i += 1


def yaml_escape(s):
    """Escape a string for YAML double-quoted value."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    entries = load_tweets(TWEETS_JS)
    tweets = [e["tweet"] for e in entries]

    # Sort chronologically (oldest first)
    tweets.sort(key=lambda t: parse_date(t["created_at"]))

    skipped_rt = 0
    written = 0
    existing_paths = set()

    os.makedirs(POSTS_DIR, exist_ok=True)

    for tweet in tweets:
        full_text = tweet["full_text"]

        # Skip retweets
        if full_text.startswith("RT @"):
            skipped_rt += 1
            continue

        # Skip replies to other tweets
        if tweet.get("in_reply_to_status_id_str"):
            continue

        tweet_id = tweet["id_str"]
        created_at = parse_date(tweet["created_at"])
        date_str = created_at.strftime("%Y-%m-%d")
        date_yaml = created_at.strftime("%Y-%m-%d %H:%M:%S %z")

        # Expand URLs in text
        entities = tweet.get("entities", {})
        urls = entities.get("urls", [])
        media = (
            tweet.get("extended_entities", {}).get("media")
            or entities.get("media", [])
        )

        text = full_text
        # Replace media t.co URLs with markdown images (before URL expansion)
        if media:
            text = replace_media_urls(text, media)
        # Expand regular t.co URLs
        text = expand_urls(text, urls)

        original_url = f"https://twitter.com/{USERNAME}/status/{tweet_id}"
        title = make_title(text)
        slug = slugify(title) or f"tweet-{tweet_id}"
        path = unique_path(POSTS_DIR, date_str, slug, existing_paths)
        existing_paths.add(path)

        is_reply = bool(tweet.get("in_reply_to_status_id_str"))
        category = "tweet"

        frontmatter = (
            f"---\n"
            f'date: {date_yaml}\n'
            f'title: "{yaml_escape(title)}"\n'
            f"category: {category}\n"
            f"original_url: {original_url}\n"
            f"---\n"
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(frontmatter)
            f.write("\n")
            f.write(text.strip())
            f.write("\n")

        written += 1

    print(f"Written: {written} posts")
    print(f"Skipped (retweets): {skipped_rt}")


if __name__ == "__main__":
    main()
