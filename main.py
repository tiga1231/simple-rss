# pip install feedparser
import feedparser


def parse_rss(url: str):
    feed = feedparser.parse(url)

    if feed.bozo:
        raise ValueError(f"Failed to parse RSS feed: {feed.bozo_exception}")

    print(f"Feed title: {feed.feed.get('title', 'Untitled')}\n")

    for entry in feed.entries:
        print("Title:", entry.get("title", "No title"), end="\n-------\n")
        print("Link:", entry.get("link", "No link"), end="\n-------\n")
        print("Published:", entry.get("published", "No date"), end="\n-------\n")
        print("Summary:", entry.get("summary", "No summary")[:300], end="\n-------\n")
        print("=" * 80)


if __name__ == "__main__":
    parse_rss("https://hnrss.org/best")
