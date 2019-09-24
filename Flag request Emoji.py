num = str(input("country flag:"))
import requests
import json
url = "https://api.coinbase.com/v2/prices/spot?currency=KRW"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
amount_data = parsed["data"]["amount"]
y = (str(amount_data))
print ("#bitcoin ","South Korean Won" ,"price:","‎₩"+str(y))