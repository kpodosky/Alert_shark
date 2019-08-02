import requests
import json

#BTC API provider URL
current_price_url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key=c90bc111bb6bc5691c8a7eba405e597de329492c5ab417782d68984b504d590f'

#All time high hardcoded. [TODO] fetch from an endpoint
ATH = 19783.06

def get_current_price():
    """Fetch BTC data from API provider

    :return: :class:`USD ticker` object
    :rtype: dict
    """
    resp = requests.get(current_price_url)
    data = {'USD' : 10199.25}
    if resp is not None and resp.status_code == 200:
        data = json.loads(resp.text)
    return data['USD']
