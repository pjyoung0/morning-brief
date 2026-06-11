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

아래 내용을 반드시 작성

━━━━━━━━━━━━━━━━━━

[국내 AI 밸류체인 현황]

종목별

전일 등락률
외국인 5일 누적 순매수
기관 5일 누적 순매수

━━━━━━━━━━━━━━━━━━

[섹터 수급 순위]

외국인 순매수 기준

1위
2위
3위

기관 순매수 기준

1위
2위
3위

━━━━━━━━━━━━━━━━━━

[오늘 가장 강한 AI 밸류체인]

근거

━━━━━━━━━━━━━━━━━━

[오늘 가장 약한 AI 밸류체인]

근거

==================

형식

1. Overnight Market

2. AI Sector Flow

3. Today Korea Watchlist

4. Important Disclosure

5. 수급 분석

종목별

- 외국인 연속 순매수 일수
- 기관 연속 순매수 일수
- 투자 시사점

6. PM Comment

실제 펀드매니저가 작성하는
아침 브리프처럼 간단하고 일목요연하게 작성

7. 정리
외국인과 기관이 동시에 순매수 중인 종목을 우선순위로 정렬하고
미국 AI 섹터 흐름과 연결해서
오늘 가장 주목할 종목 TOP5를 선정해라.

"""

    response = model.generate_content(
        prompt
    )

    return response.text
