import feedparser

RSS_FEEDS = [

    "NVDA":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=NVDA&region=US&lang=en-US",

    "AMD":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AMD&region=US&lang=en-US",

    "AVGO":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AVGO&region=US&lang=en-US",

    "MRVL":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=MRVL&region=US&lang=en-US",

    "TSM":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=TSM&region=US&lang=en-US",

    "ASML":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ASML&region=US&lang=en-US",

    "AMAT":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AMAT&region=US&lang=en-US",

    "LRCX":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=LRCX&region=US&lang=en-US",

    "SMCI":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=SMCI&region=US&lang=en-US",

    "VRT":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=VRT&region=US&lang=en-US",

    "ETN":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ETN&region=US&lang=en-US",

    "COHR":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=COHR&region=US&lang=en-US",

    "TSLA":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=TSLA&region=US&lang=en-US",

    "ANET":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ANET&region=US&lang=en-US",

    "MSFT":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=MSFT&region=US&lang=en-US",

    "AMZN":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AMZN&region=US&lang=en-US",

    "GOOGL":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=GOOGL&region=US&lang=en-US",

    "ISRG":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ISRG&region=US&lang=en-US",

    "KLAC":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=KLAC&region=US&lang=en-US",

    "LITE":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=LITE&region=US&lang=en-US",

    "RTX":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=RTX&region=US&lang=en-US",

    "LMT":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=LMT&region=US&lang=en-US",
    
    "SMR":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=SMR&region=US&lang=en-US",

    "OKLO":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=OKLO&region=US&lang=en-US",
    
    "ORCL":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ORCL&region=US&lang=en-US",
    
    "CRWV":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=CRWV&region=US&lang=en-US",

    "NBIS":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=NBIS&region=US&lang=en-US",
    
    "ELF":
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ELF&region=US&lang=en-US"
]


def get_news_data():

    result = ""

    for ticker, url in RSS_FEEDS.items():

        try:

            feed = feedparser.parse(url)

            if len(feed.entries) == 0:
                continue

            title = feed.entries[0].title

            result += (
                f"{ticker}\n"
                f"뉴스: {title}\n\n"
            )

        except Exception as e:

            print(
                ticker,
                e
            )

    return result
