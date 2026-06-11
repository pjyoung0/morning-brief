import os

from pykrx import stock

from datetime import datetime
from datetime import timedelta

KRX_ID = os.environ["KRX_ID"]

KRX_PW = os.environ["KRX_PW"]

WATCHLIST = {

    "SK하이닉스":"000660",
    "삼성전자":"005930",

    "주성엔지니어링":"036930",

    "HPSP":"403870",

    "한미반도체":"042700",

    "삼성전기":"009150",

    "HD현대일렉트릭":"267260",

    "대한광통신":"010170",

    "솔브레인":"357780",

    "NAVER":"035420",

    "레인보우로보틱스":"277810"
}

SECTOR_MAP = {

    "HBM·메모리":[
        "SK하이닉스",
        "삼성전자"
    ],

    "전공정 장비":[
        "주성엔지니어링"
    ],

    "전공정 검사":[
        "HPSP"
    ],

    "후공정·패키징":[
        "한미반도체"
    ],

    "PCB":[
        "삼성전기"
    ],

    "전력기기":[
        "HD현대일렉트릭"
    ],

    "광통신":[
        "대한광통신"
    ],

    "소부장 소재":[
        "솔브레인"
    ],

    "클라우드":[
        "NAVER"
    ],

    "AI로봇":[
        "레인보우로보틱스"
    ]
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

            price_df = stock.get_market_ohlcv_by_date(
                start_str,
                end_str,
                ticker
            )

            change_pct = round(
                (
                    price_df["종가"].iloc[-1]
                    /
                    price_df["종가"].iloc[-2]
                    - 1
                ) * 100,
                2
            )

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

                "전일등락률": change_pct,

                "외국인5일": foreign_5d,

                "기관5일": institution_5d

            })

        except Exception as e:

            print(
                name,
                e
            )

    sector_result = {}

    for sector, stocks in SECTOR_MAP.items():

    foreign_sum = 0

    institution_sum = 0

    for item in result:

        if item["종목"] in stocks:

            foreign_sum += item["외국인5일"]

            institution_sum += item["기관5일"]

    sector_result[sector] = {

        "외국인": round(foreign_sum,1),

        "기관": round(institution_sum,1)

    }
    
    return {

    "stocks": result,

    "sectors": sector_result

}
