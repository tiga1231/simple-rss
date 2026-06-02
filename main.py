# pip install feedparser
import feedparser


def parse_rss(url: str):
    feed = feedparser.parse(url)

    if feed.bozo:
        raise ValueError(f"Failed to parse RSS feed: {feed.bozo_exception}")

    print(f"Feed title: {feed.feed.get('title', 'Untitled')}\n")

    for entry in feed.entries:
        # print(entry.keys())
        # break
        print("Title:", entry.get("title", "No title"))
        print("-" * 3)
        print("Link:", entry.get("link", "No link"))
        print("Published:", entry.get("published", "No date"))
        print("Summary:", entry.get("summary", "No summary"))
        print()


if __name__ == "__main__":
    parse_rss("https://hnrss.org/best")
