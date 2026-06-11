from pykrx import stock

from datetime import datetime
from datetime import timedelta

WATCHLIST = {

    "삼성전자":"005930",
    "SK하이닉스":"000660",

    "삼성전기":"009150",

    "LS ELECTRIC":"010120",

    "성호전자":"043260",

    "심텍":"222800",

    "코리아써키트":"007810",

    "유진테크":"084370",

    "원익IPS":"240810",

    "한미반도체":"042700",

    "기가비스":"420770",

    "리노공업":"058470",

    "HPSP":"403870"
}

def count_consecutive_buy(series):

    count = 0

    for value in reversed(series):

        if value > 0:
            count += 1
        else:
            break

    return count

def get_flow_data():

    end_date = datetime.today()

    start_date = (
        end_date
        - timedelta(days=15)
    )

    start_str = (
        start_date.strftime("%Y%m%d")
    )

    end_str = (
        end_date.strftime("%Y%m%d")
    )

    result = []

    for name, ticker in WATCHLIST.items():

        try:

            df = stock.get_market_trading_value_by_date(
                start_str,
                end_str,
                ticker
            )

            foreign = df["외국인합계"]

            institution = df["기관합계"]

            foreign_5d = (
                foreign.tail(5).sum()
                / 100000000
            )

            institution_5d = (
                institution.tail(5).sum()
                / 100000000
            )

            foreign_streak = (
                count_consecutive_buy(
                    foreign
                )
            )

            institution_streak = (
                count_consecutive_buy(
                    institution
                )
            )

            result.append({

                "종목": name,

                "외국인5일":
                round(
                    foreign_5d,
                    1
                ),

                "기관5일":
                round(
                    institution_5d,
                    1
                ),

                "외국인연속":
                foreign_streak,

                "기관연속":
                institution_streak

            })

        except Exception as e:

            print(
                name,
                e
            )

    return result
