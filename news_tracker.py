import yfinance as yf

NEWS_TICKERS = {

    "NVDA":"AI_CHIP",

    "AVGO":"AI_CHIP",

    "MRVL":"AI_CHIP",

    "TSM":"Foundry",

    "ASML":"Front_End_Equipment",

    "KLAC":"Front_End_Equipment",

    "VRT":"Power",

    "ETN":"Power",

    "COHR":"Optical",

    "LITE":"Optical",

    "TSLA":"AI_ROBOT",

    "RTX":"Defense",

    "LMT":"Defense",

    "SMR":"SMR",

    "OKLO":"SMR",

    "ELF":"Cosmetics"

}

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
                f"\n[{sector}]\n"
                f"{ticker}\n"
                f"{title}\n"
            )

        except Exception as e:

            print(
                ticker,
                e
            )

    return result
