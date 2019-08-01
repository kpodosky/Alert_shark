import requests
import json

current_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key=c90bc111bb6bc5691c8a7eba405e597de329492c5ab417782d68984b504d590f'
ATH = 19783.06

def get_current_price():
    resp = requests.get(current_price_url)
    data = {'USD' : 10199.25}
    if resp is not None and resp.status_code == 200:
        data = json.loads(resp.text)
    return data['USD']
