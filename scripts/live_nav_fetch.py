import requests
import pandas as pd

schemes = {
    "119551": "sbi_bluechip",
    "120503": "icici_bluechip",
    "118632": "nippon_largecap",
    "119092": "axis_bluechip",
    "120841": "kotak_bluechip"
}

for code, name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

    print(f"{name} saved")