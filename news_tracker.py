import feedparser

NEWS_KEYWORDS = [

    "NVIDIA",

    "Broadcom",

    "Marvell",

    "TSMC",

    "ASML",

    "Vertiv",

    "Eaton",

    "Coherent",

    "Tesla"
]

def get_news_data():

    result = ""

    for ticker, sector in NEWS_TICKERS.items():

        try:

            stock = yf.Ticker(ticker)

            news = stock.news

            if len(news) == 0:
                continue

            article = news[0]

            title = article["title"]

            result += (
                f"\n[{sector}] "
                f"{ticker}\n"
                f"뉴스: {title}\n"
            )

        except Exception as e:

            print(
                ticker,
                e
            )

    return result
  
