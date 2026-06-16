import feedparser

RSS_FEEDS = [

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=NVDA&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AVGO&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=MRVL&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=TSM&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ASML&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=VRT&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ETN&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=COHR&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=TSLA&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=KLAC&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=LITE&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=RTX&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=LMT&region=US&lang=en-US",
    
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=SMR&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=OKLO&region=US&lang=en-US",

    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=ELF&region=US&lang=en-US"
]


def get_news_data():

    result = ""

    for url in RSS_FEEDS:

        try:

            feed = feedparser.parse(url)

            entries = feed.entries[:3]

            for item in entries:

                result += (

                    f"제목: {item.title}\n"

                )

        except Exception as e:

            print(e)

    return result
