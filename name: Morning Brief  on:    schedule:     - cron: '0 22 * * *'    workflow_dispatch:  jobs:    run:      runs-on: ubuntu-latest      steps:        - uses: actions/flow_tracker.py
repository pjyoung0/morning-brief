from pykrx import stock
from datetime import datetime, timedelta

def get_consecutive_buy_stocks():

    end_date = datetime.today()

    start_date = end_date - timedelta(days=10)

    end_str = end_date.strftime("%Y%m%d")
    start_str = start_date.strftime("%Y%m%d")

    result = []

    tickers = stock.get_market_ticker_list(
        market="KOSPI"
    )

    for ticker in tickers[:200]:

        try:

            df = stock.get_market_trading_value_by_date(
                start_str,
                end_str,
                ticker
            )

            if len(df) < 5:
                continue

            foreign = df["외국인합계"]

            institution = df["기관합계"]

            foreign_5d = all(
                foreign.tail(5) > 0
            )

            institution_3d = all(
                institution.tail(3) > 0
            )

            if foreign_5d:

                result.append({
                    "종목":
                    stock.get_market_ticker_name(
                        ticker
                    ),
                    "외국인":
                    True,
                    "기관":
                    institution_3d
                })

        except:
            pass

    return result
