import os

from pykrx import stock

from datetime import datetime
from datetime import timedelta

KRX_ID = os.environ["KRX_ID"]

KRX_PW = os.environ["KRX_PW"]

WATCHLIST = {

    "SK하이닉스":"000660",
    "삼성전자":"005930",
    "한미반도체":"042700",

    "주성엔지니어링":"036930",
    "원익IPS":"240810",
    "테스":"095610",
    "피에스케이":"319660",
    "넥스틴":"348210",
    "파크시스템스":"140860",
    "브이엠":"089970",  
    "HPSP":"403870",

    "동진쎄미켐":"005290",
    "한솔케미칼":"014680",
    "원익머트리얼즈":"104830",
    "하나머티리얼즈":"166090",
    "원익QnC":"074600",
    "이엔에프테크놀로지":"102710",
    "솔브레인":"357780",
    "하나마이크론":"067310",
    "코미코":"183300",
    "인텍플러스":"064290",
    "테크윙":"089030",
    "기가비스":"420770",
    "리노공업":"058470",
    "고영":"098460",
    "두산테스나":"131970",
    "티씨케이":"064760",

    "가온칩스":"399720",
    "DB하이텍":"000990",
    "에이직랜드":"445090",
    "HD현대일렉트릭":"267260",

    "이수페타시스":"007660",
    "대덕전자":"353200",
    "LG이노텍":"011070",
    "심텍":"222800",
    "코리아써키트":"007810",
    "삼성전기":"009150",

    "효성중공업":"298040",
    "LS ELECTRIC":"010120",
    "일진전기":"103590",
    "가온전선":"000500",

    "대한광통신":"010170",
    "성호전자":"043260",
    "에치에프알":"230240",
    "머큐리":"100590",
    "다산네트웍스":"039560",
    "오이솔루션":"138080",
    "코스텍시스":"355150",

    "KT":"030200",
    "SK텔레콤":"017670",
    "LG CNS":"064400",
    "케이아이엔엑스":"093320",
    "가비아":"079940",

    "NAVER":"035420",
    "카카오":"035720",
    "삼성SDS":"018260",

    "레인보우로보틱스":"277810",
    "두산로보틱스":"454910",
    "로보스타":"090360",
    "로보티즈":"108490",

    "루닛":"328130",
    "현대오토에버":"307950"
}

SECTOR_MAP = {

    "HBM·메모리":[
        "SK하이닉스",
        "삼성전자"
    ],

    "AI칩":[
        "SK하이닉스",
        "삼성전자",
        "한미반도체"
    ],

    "AI 커스텀칩":[
        "삼성전자",
        "삼성전기",
        "가온칩스",
        "에이직랜드"
    ],


    "전공정 장비":[
        "주성엔지니어링",
        "원익IPS",
        "테스",
        "피에스케이",
        "넥스틴",
        "브이엠"
    ],

    "전공정 검사":[
        "HPSP",
        "파크시스템스"
    ],

    "소부장 소재":[
        "동진쎄미켐",
        "한솔케미칼",
        "원익머트리얼즈",
        "하나머티리얼즈",
        "원익QnC",
        "이엔에프테크놀로지",
        "솔브레인",
        "티씨케이"
    ],
    
    "후공정·패키징":[
        "한미반도체",
        "하나마이크론",
        "코미코",
        "인텍플러스",
        "테크윙",
        "기가비스",
        "리노공업",
        "고영",
        "두산테스나"
    ],

    "PCB":[
        "이수페타시스",
        "대덕전자",
        "LG이노텍",
        "심텍",
        "코리아써키트",
        "삼성전기"
    ],

    "전력기기":[
        "HD현대일렉트릭",
        "효성중공업",
        "LS ELECTRIC",
        "일진전기",
        "가온전선"
    ],

    "광통신":[
        "대한광통신",
        "성호전자",
        "에치에프알",
        "머큐리",
        "다산네트웍스",
        "오이솔루션",
        "코스텍시스"
    ],

    "데이터센터":[
        "KT",
        "SK텔레콤",
        "LG CNS",
        "케이아이엔엑스",
        "가비아"
    ],

    "클라우드":[
        "NAVER",
        "카카오",
        "삼성SDS",
        "LG CNS"
    ],

    "AI로봇":[
        "레인보우로보틱스",
        "두산로보틱스",
        "로보스타",
        "로보티즈"
    ]
    
    "AI의료":[
        "루닛"
    ],

    "자율주행":[
        "현대오토에버"
    ]
}


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

            print(name)
            
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


            result.append({

                "종목": name,

                "전일등락률": change_pct,

                "외국인5일":
                    round(foreign_5d,1),

                "기관5일": 
                    round(institution_5d,1),

                "합산":
                    round(
                        foreign_5d +
                        institution_5d,
                        1
                    )

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
    
    foreign_rank = sorted(
        sector_result.items(),
        key=lambda x: x[1]["외국인"],
        reverse=True
    )

    institution_rank = sorted(
        sector_result.items(),
        key=lambda x: x[1]["기관"],
        reverse=True
    )

    
    return {

        "stocks": result,

        "sectors": sector_result,

        "foreign_rank":
            foreign_rank[:3],

        "institution_rank":
            institution_rank[:3]

}
