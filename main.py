from us_market import get_market_data

from ai_sector import (
    get_sector_data,
    get_korea_watchlist
)

from dart_disclosure import (
    get_dart_disclosure
)

from gemini_report import (
    generate_report
)

from email_sender import (
    send_email
)

from flow_tracker import (
    get_flow_data
)

market = get_market_data()
print("미국시장 수집 완료")

sector = get_sector_data()
print("AI 섹터 수집 완료")

watchlist = get_korea_watchlist()
print("국내 관심종목 생성 완료")

dart = get_dart_disclosure()
print("DART 수집 완료")

flow_data = get_flow_data()
print("수급 수집 완료")

report = generate_report(

    market,
    sector,
    watchlist,
    dart,
    flow_data
)


print(report)

send_email(report)
