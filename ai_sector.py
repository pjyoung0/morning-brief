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
            "삼성전자",
            "삼성전기"
        ]
    },

    "파운드리·전공정": {
        "us": [
            "TSM"
        ],
        "kr": [
            "주성엔지니어링",
            "원익IPS",
            "삼성전자"
        ]
    },

    "전공정 검사": {
        "us": [
            "KLAC"
        ],
        "kr": [
            "HPSP"
        ]
    },

    "PCB": {
        "us": [
            "SMCI"
        ],
        "kr": [
            "이수페타시스",
            "삼성전기"
        ]
    },

    "전력기기": {
        "us": [
            "VRT",
            "ETN"
        ],
        "kr": [
            "HD현대일렉트릭",
            "효성중공업"
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
            "레인보우로보틱스"
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
