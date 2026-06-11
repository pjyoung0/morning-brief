import os
import google.generativeai as genai

genai.configure(
    api_key=os.environ[
        "GEMINI_API_KEY"
    ]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_report(
    market_data,
    sector_data,
    watchlist,
    dart_data,
    flow_data
):

    prompt = f"""

당신은 국내 자산운용사 펀드매니저다.

다음 정보를 보고
오전 7시 모닝브리프를 작성해라.

==================

미국시장

{market_data}

==================

AI 섹터

{sector_data}

==================

국내 관심종목

{watchlist}

==================

DART 공시

{dart_data}

==================

수급 데이터

{flow_data}

==================

형식

1. Overnight Market

2. AI Sector Flow

3. Today Korea Watchlist

4. Important Disclosure

5. 수급 분석
외국인 연속 순매수
기관 연속 순매수
동시 순매수
투자 시사점

6. PM Comment

실제 펀드매니저가 작성하는
아침 브리프처럼 간단하고 일목요연하게 작성

"""

    response = model.generate_content(
        prompt
    )

    return response.text
