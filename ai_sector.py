import yfinance as yf

AI_SECTORS = {

    "반도체":[
        "NVDA",
        "AMD",
        "AVGO",
        "MRVL"
    ],

    "광통신":[
        "COHR",
        "LITE",
        "AAOI"
    ],

    "전력기기":[
        "VRT",
        "ETN",
        "PWR"
    ]
}

def get_sector_data():

    result = {}

    for sector, tickers in AI_SECTORS.items():

        detail = {}

        for ticker in tickers:

            hist = yf.Ticker(ticker).history(period="5d")

            close = hist["Close"]

            pct = (
                close.iloc[-1]
                / close.iloc[-2]
                - 1
            ) * 100

            detail[ticker] = round(pct,2)

        result[sector] = detail

    return result
