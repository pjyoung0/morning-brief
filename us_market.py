import yfinance as yf

INDICES = {
    "S&P500": "^GSPC",
    "NASDAQ": "^IXIC",
    "Russell2000": "^RUT",
    "SOXX":"SOXX",
    "USD/KRW": "KRW=X",
    "WTI": "CL=F"
}

def get_market_data():

    result = {}

    for name, ticker in INDICES.items():

        hist = yf.Ticker(ticker).history(period="5d")

        close = hist["Close"]

        pct = (
            close.iloc[-1]
            / close.iloc[-2]
            - 1
        ) * 100

        result[name] = round(pct, 2)

    return result
