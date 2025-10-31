import requests
r = requests.get('https://remoteok.com/api', headers={'User-Agent': 'Mozilla/5.0'})
data = r.json()
print(f'API works: Got {len(data)} total entries')
if len(data) > 1:
    print(f'First job: {data[1].get("position", "N/A")} at {data[1].get("company", "N/A")}')
    print(f'URL: https://remoteok.com{data[1].get("url", "")}')

