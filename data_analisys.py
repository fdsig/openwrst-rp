import pandas as pd
import json

with open('./speedtests.json', 'r') as f:
        data = json.load(f)

data = [
        {k:v for k,v in kv.items() if k in ['download', 'upload', 'ping', 'ssid']} for kv in data
]
print(data)
# drop unknown ssid
data = [i for i in data if i.get('ssid') is not None and i['ssid'] != 'unknown']

df = pd.DataFrame(data)
df = df.groupby('ssid').agg({'download': 'mean', 'upload': 'mean', 'ping': 'mean'})

# 1 decimal place and convert to MB/s
df.download = df.download.round(1)
df.upload = df.upload.round(1)
df.ping = df.ping.round(1)
# change ssid to [f'ssid_{i}' for i in range(len(df))]
#df.index = ['Rasberry_pi', 'NanoPi_R2S', 'Home_router']

print(df)
