import os
from datetime import datetime
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

    today = datetime.now().strftime(
    "%Y-%m-%d"
)
    prompt = f"""

오늘 날짜는 {today}이다.

당신은 국내 롱온리 자산운용사 펀드매니저다.

절대로 존재하지 않는 날짜를 생성하지 말 것.
모든 날짜는 반드시 오늘 날짜 기준으로 작성할 것.
수신, 발신, 일시를 작성하지 말 것.

다음 정보를 보고
오전 7시 모닝브리프를 작성해라.

====================
Overnight Market
====================

{market_data}

====================
US AI Sector Flow
====================

{sector_data}

====================
Korea Watchlist
====================

{watchlist}

====================
DART Disclosure
====================

{dart_data}

====================
Flow Data
====================

{flow_data}

====================

반드시 아래 순서로 작성

━━━━━━━━━━━━━━━━━━

현재 생성시각:
{datetime.now()}

오늘 날짜는 {today}

1. Overnight Market

아래 지수들을 반드시 포함할 것.
- S&P500
- NASDAQ
- Russell2000
- SOXX
- KOSPI200 야간선물
- USD/KRW 환율
- WTI 유가

요약하여 전망 작성

━━━━━━━━━━━━━━━━━━

2. AI Sector Flow

아래 섹터별로 작성

AI칩
AI 커스텀칩
파운드리·전공정
전공정 검사
PCB
전력기기
광통신
AI 로봇

각 섹터마다

- 미국 대표 기업 등락률
- 섹터 강도 평가
- 국내 수혜주

작성

━━━━━━━━━━━━━━━━━━

3. Today Korea Watchlist

오늘 가장 중요한 섹터 TOP3 선정

각 섹터별

왜 중요한지
어떤 종목을 봐야하는지

작성


━━━━━━━━━━━━━━━━━━

4. Important Disclosure

전일 DART 공시 중

실제 투자 관점에서 중요한 것만 정리

━━━━━━━━━━━━━━━━━━

5. 수급 분석

수급은 반드시 보조지표로만 사용. 최종 추천에서도 보조로만 활용할 것.

섹터별

외국인 최근 5일 누적 순매수
기관 최근 5일 누적 순매수

상위 3개 섹터만 작성

예시

외국인 순매수 TOP3

1위 HBM·메모리
2위 전력기기
3위 PCB

기관 순매수 TOP3

1위 광통신
2위 후공정
3위 전공정

━━━━━━━━━━━━━━━━━━

6. PM Comment

운용역 관점 코멘트

5~10줄

오늘 시장에서

어떤 섹터가 강할지
어떤 섹터가 약할지
어디에 자금이 몰릴 가능성이 높은지

작성

━━━━━━━━━━━━━━━━━━

7. 정리

오늘 가장 주목할 종목 TOP5

순위
종목
근거

형태로 작성

━━━━━━━━━━━━━━━━━━

중요

절대로

##
###
**
마크다운 사용 금지

메일처럼 깔끔하게 작성

"""


    response = model.generate_content(
        prompt
    )

    return response.text
