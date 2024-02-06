#!/usr/env/python3

import json
import pandas as pd

url = "http://storage.googleapis.com/play_public/supported_devices.csv"

df = pd.read_csv(url, encoding="utf-16")

devices = []

for line in df.itertuples():
    retail_branding = str(line[1])
    marketing_name = str(line[2])
    device = str(line[3])
    model = str(line[4])

    if marketing_name.lower().startswith(retail_branding.lower()):
        name = f"{marketing_name} ({model})"
    elif marketing_name.lower() == retail_branding.lower():
        name = f"{retail_branding} {model}"
    else:
        name = f"{retail_branding} {marketing_name} ({model})"

    devices.append(
        {
            "codename": device,
            "retail_branding": retail_branding,
            "marketing_name": marketing_name,
            "model": model,
            "name": name,
        }
    )

with open("devices.json", "w") as f:
    f.write(json.dumps(devices).replace("},", "},\n"))
