import os
import requests
from datetime import datetime, timedelta

API_KEY = os.environ["DART_API_KEY"]

IMPORTANT = [

    "공급계약",
    "수주",
    "전환사채",
    "유상증자",
    "신규시설투자"
]

def get_dart_disclosure():

    yesterday = (
        datetime.now()
        - timedelta(days=1)
    ).strftime("%Y%m%d")

    url = (
        "https://opendart.fss.or.kr/api/list.json"
    )

    params = {

        "crtfc_key": API_KEY,
        "bgn_de": yesterday,
        "end_de": yesterday,
        "page_count": 100
    }

    r = requests.get(
        url,
        params=params
    )

    data = r.json()

    result = []

    if "list" not in data:
        return []

    for item in data["list"]:

        title = item["report_nm"]

        if any(
            x in title
            for x in IMPORTANT
        ):

            result.append(
                f"{item['corp_name']} | {title}"
            )

    return result[:20]
