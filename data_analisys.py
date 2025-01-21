import pandas as pd
import json

with open('./speedtests.json', 'r') as f:
        data = json.load(f)

data = [
        {k:v for k,v in kv.items() if k in ['download', 'upload', 'ping', 'ssid']} for kv in data
]

df = pd.DataFrame(data)

print(df)
