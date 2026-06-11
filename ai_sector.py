import yfinance as yf

AI_SECTORS = {

    "AI칩": {
        "us":[
            "NVDA",
            "AMD"
        ],
        "kr":[
            "SK하이닉스",
            "삼성전자",
            "한미반도체"
        ]
    },

    "AI 커스텀칩":{
        "us":[
            "AVGO",
            "MRVL"
        ],
        "kr":[
            "삼성전자",
            "삼성전기"
        ]
    },

    "파운드리·전공정":{
        "us":[
            "TSM"
        ],
        "kr":[
            "주성엔지니어링",
            "원익IPS",
            "삼성전자"
        ]
    },

    "전공정 검사":{
        "us":[
            "KLAC"
        ],
        "kr":[
            "HPSP"
        ]
    },

    "PCB":{
        "us":[
            "SMCI"
        ],
        "kr":[
            "이수페타시스",
            "삼성전기"
        ]
    },

    "전력기기":{
        "us":[
            "VRT",
            "ETN"
        ],
        "kr":[
            "HD현대일렉트릭",
            "효성중공업"
        ]
    },

    "광통신":{
        "us":[
            "COHR",
            "LITE"
        ],
        "kr":[
            "대한광통신",
            "성호전자",
            "에치에프알"
        ]
    },

    "AI 로봇":{
        "us":[
            "TSLA"
        ],
        "kr":[
            "레인보우로보틱스"
        ]
    }
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

KOREA_MAPPING = {

    "반도체":[
        "SK하이닉스",
        "한미반도체",
        "브이엠",
        "테크윙",
        "ISC"
    ],

    "광통신":[
        "오이솔루션",
        "성호전",
        "대한광통신"
    ],

    "전력기기":[
        "HD현대일렉트릭",
        "LS ELECTRIC",
        "효성중공업",
        "산일전기"
    ]
}

def get_korea_watchlist():

    sector_data = get_sector_data()

    watchlist = {}

    for sector, detail in sector_data.items():

        avg_return = (
            sum(detail.values())
            / len(detail)
        )

        if avg_return > 0:

            watchlist[sector] = (
                KOREA_MAPPING.get(
                    sector,
                    []
                )
            )

    return watchlist
