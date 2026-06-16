import yfinance as yf

ETFS = {

    "반도체":[
        "SOXX",
        "SMH",
        "SOXL",
        "AIQ"
    ],

    "전력":[
        "GRID",
        "COPX"
    ],

    "광통신":[
        "FIVG"
    ],

    "바이오":[
        "XBI",
        "IBB"
    ],

    "방산":[
        "ITA"
    ],

    "피지컬AI":[
        "ARKX"
    ],

    "에너지":[
        "URA",
        "XLE"
    ]
}


NEWS_MAP = {

    "NVDA":
        "AI 데이터센터 투자 확대",

    "AMD":
        "AI GPU 수요 증가",

    "AVGO":
        "AI ASIC 수요 확대",

    "MRVL":
        "커스텀칩 수주 기대",

    "TSM":
        "첨단공정 생산 확대",

    "KLAC":
        "반도체 검사장비 투자 증가",

    "SMCI":
        "AI 서버 수요 증가",

    "VRT":
        "데이터센터 전력 수요 증가",

    "ETN":
        "전력 인프라 투자 확대",

    "COHR":
        "광통신 수요 증가",

    "LITE":
        "광모듈 수요 증가",

    "TSLA":
        "휴머노이드 로봇 기대"
}


SECTORS = {

    "AI칩": {
        "us": [
            "NVDA",
            "AMD"
        ],
        "kr": [
            "SK하이닉스",
            "삼성전자",
            "한미반도체"
        ]
    },

    "AI 커스텀칩": {
        "us": [
            "AVGO",
            "MRVL"
        ],
        "kr": [
            "삼성전기",
            "가온칩스",
            "LG이노텍"
        ]
    },

    "파운드리·전공정": {
        "us": [
            "TSM",
            "AMAT",
            "LRCX"
        ],
        "kr": [
            "주성엔지니어링",
            "원익IPS",
            "HPSP",
            "유진테크"
        ]
    },

    "전공정 검사": {
        "us": [
            "KLAC"
        ],
        "kr": [
            "파크시스템스",
            "넥스틴"
        ]
    },

    "PCB": {
        "us": [
            "AVGO",
            "TTM"
        ],
        "kr": [
            "이수페타시스",
            "삼성전기",
            "대덕전자",
            "심텍",
            "LG이노텍"
        ]
    },

    "전력기기": {
        "us": [
            "VRT",
            "ETN"
        ],
        "kr": [
            "HD현대일렉트릭",
            "효성중공업",
            "LS일렉트릭"
        ]
    },

    "광통신": {
        "us": [
            "COHR",
            "LITE"
        ],
        "kr": [
            "대한광통신",
            "성호전자",
            "에치에프알"
        ]
    },

    "AI 로봇": {
        "us": [
            "TSLA"
        ],
        "kr": [
            "레인보우로보틱스",
            "두산로보틱스",
            "로보티즈"
        ]
    },

    "방산": {
        "us": [
            "RTX",
            "LMT",
            "NOC"
        ],
        "kr": [
            "한화에어로스페이스",
            "LIG넥스원"
        ]
    },

    "원전·SMR": {
        "us": [
            "SMR",
            "OKLO",
            "URA"
        ],
        "kr": [
            "두산에너빌리티",
            "한전기술"
        ]
    },

    "바이오": {
        "us": [
            "XBI"
        ],
        "kr": [
            "셀트리온",
            "삼성바이오로직스"
        ]
    },

    "중동재건": {
        "us": [
            "WTI"
        ],
        "kr": [
            "현대건설",
            "삼성물산"
        ]
    },

    "화장품": {
        "us": [
            "ELF"
        ],
        "kr": [
            "에이피알",
            "한국콜마"
        ]
    }

}


def get_sector_data():

    result = ""

    for sector, data in SECTORS.items():

        result += f"\n[{sector}]\n"

        total_change = 0

        count = 0

        for ticker in data["us"]:

            try:

                stock = yf.Ticker(ticker)

                hist = stock.history(
                    period="5d"
                )

                change = round(
                    (
                        hist["Close"].iloc[-1]
                        /
                        hist["Close"].iloc[-2]
                        - 1
                    ) * 100,
                    2
                )

                reason = NEWS_MAP.get(
                    ticker,
                    "특이 뉴스 없음"
                )

                result += (
                    f"{ticker}: "
                    f"{change}% "
                    f"({reason})\n"
                )

                total_change += change

                count += 1

            except Exception as e:

                print(
                    ticker,
                    e
                )

        if count > 0:

            avg = round(
                total_change / count,
                2
            )

        else:

            avg = 0

        result += (
            f"섹터 평균: "
            f"{avg}%\n"
        )

        if sector in ETFS:

            result += "\n대표 ETF\n"

            for etf in ETFS[sector]:

                try:

                    hist = yf.Ticker(
                        etf
                    ).history(
                        period="5d"
                    )

                    etf_change = round(
                        (
                            hist["Close"].iloc[-1]
                            /
                            hist["Close"].iloc[-2]
                            - 1
                        ) * 100,
                        2
                    )

                    result += (
                        f"{etf}: "
                        f"{etf_change}%\n"
                    )

                except:

                    pass

        result += (
            "\n국내 연관주\n"
        )

        for stock_name in data["kr"]:

            result += (
                f"- {stock_name}\n"
            )

        result += "\n"

    return result

def get_korea_watchlist():

    text = ""

    for sector, data in SECTORS.items():

        text += (
            f"\n[{sector}]\n"
        )

        for stock_name in data["kr"]:

            text += (
                f"- {stock_name}\n"
            )

    return text
