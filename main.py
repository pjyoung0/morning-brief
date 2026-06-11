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

market = get_market_data()

sector = get_sector_data()

watchlist = get_korea_watchlist()

dart = get_dart_disclosure()

report = generate_report(

    market,
    sector,
    watchlist,
    dart

)

print(report)

send_email(report)
