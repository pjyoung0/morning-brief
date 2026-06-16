import yfinance as yf

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
            "ETN",
            "EATON"
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

                hist = stock.history(period="5d")

                change = round(
                    (
                        hist["Close"].iloc[-1]
                        /
                        hist["Close"].iloc[-2]
                        - 1
                    ) * 100,
                    2
                )

                result += (
                    f"{ticker}: "
                    f"{change}%\n"
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

        result += (
            "국내 연관주:\n"
        )

        for stock_name in data["kr"]:

            result += (
                f"- {stock_name}\n"
            )

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
