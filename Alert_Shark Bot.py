import requests
import json
url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
amount_data = parsed["data"]["amount"]
Data_pro = float(amount_data)
bit_2017 = 19783.21
crease = 100
num = Data_pro/bit_2017*crease

"""this would print out the value of the current bitcion price"""

if num <= 50 :
  print ("Bitcoin","📈")
elif num >= 50 :
    print ("Bitcoin","📉" )
    

if num <= 0 :
    print ("░░░░░░░░░░░░░░░ 0%")
elif num <= 1 :
    print ("░░░░░░░░░░░░░░░ 1%")
elif num <= 2 :
    print ("░░░░░░░░░░░░░░░ 2%")
elif num <= 3 :
    print ("░░░░░░░░░░░░░░░ 3%")
elif num <= 4 :
    print ("▓░░░░░░░░░░░░░░ 4%")
elif num <= 5 :
    print ("▓░░░░░░░░░░░░░░ 5%")
elif num <= 6 :
    print ("▓░░░░░░░░░░░░░░ 6%")
elif num <= 7 : 
    print ("▓░░░░░░░░░░░░░░ 7%")
elif num <= 8 :
    print ("▓░░░░░░░░░░░░░░ 8%")
elif num <= 9 :
    print ("▓░░░░░░░░░░░░░░ 9%")
elif num <= 10 : 
    print ("▓▓░░░░░░░░░░░░░ 10%")
elif num <= 11 :
    print ("▓▓░░░░░░░░░░░░░ 11%")
elif num <= 12 :
    print ("▓▓░░░░░░░░░░░░░ 12%")
elif num <= 13 :
    print ("▓▓░░░░░░░░░░░░░ 13%")
elif num <= 14 : 
    print ("▓▓░░░░░░░░░░░░░ 14%")
elif num <= 15 :
    print ("▓▓░░░░░░░░░░░░░ 15%")
elif num <= 16 :
    print ("▓▓░░░░░░░░░░░░░ 16%")
elif num <= 17 : 
    print ("▓▓▓░░░░░░░░░░░░ 17%")
elif num <= 18 :
    print ("▓▓▓░░░░░░░░░░░░ 18%")
elif num <= 19 : 
    print ("▓▓▓░░░░░░░░░░░░ 19%")
elif num <= 20 :
    print ("▓▓▓░░░░░░░░░░░░ 20%")
elif num <= 21 :
    print ("▓▓▓░░░░░░░░░░░░ 21%")
elif num <= 22 :
    print ("▓▓▓░░░░░░░░░░░░ 22%")
elif num <= 23 :
    print ("▓▓▓░░░░░░░░░░░░ 23%")
elif num <= 24 :
    print ("▓▓▓▓░░░░░░░░░░░ 24%")
elif num <= 25 :
    print ("▓▓▓▓░░░░░░░░░░░ 25%")
elif num <= 26 :
    print("▓▓▓▓░░░░░░░░░░░ 26%")
elif num <= 27 :
    print ("▓▓▓▓░░░░░░░░░░░ 27%")
elif num <= 28 :
    print ("▓▓▓▓░░░░░░░░░░░ 28%")
elif num <= 29 :
    print ("▓▓▓▓░░░░░░░░░░░ 29%")
elif num <= 30 :
    print ("▓▓▓▓▓░░░░░░░░░░ 30%")
elif num <= 31 :
    print ("▓▓▓▓▓░░░░░░░░░░ 31%")
elif num <= 32 :
    print ("▓▓▓▓▓░░░░░░░░░░ 32%")
elif num <= 33 :
    print ("▓▓▓▓▓░░░░░░░░░░ 33%")
elif num <= 34 :
    print ("▓▓▓▓▓░░░░░░░░░░ 34%")
elif num <= 35 :
    print ("▓▓▓▓▓░░░░░░░░░░ 35%")
elif num <= 36 :
    print ("▓▓▓▓▓░░░░░░░░░░ 36%")
elif num <= 37 :
    print ("▓▓▓▓▓▓░░░░░░░░░ 37%")
elif num <= 38 :
    print ("▓▓▓▓▓▓░░░░░░░░░ 38%")
elif num <= 39 :
    print ("▓▓▓▓▓▓░░░░░░░░░ 39%")
elif num <= 40 :
    print ("▓▓▓▓▓▓░░░░░░░░░ 40%")
elif num <= 41 :
    print ("▓▓▓▓▓▓░░░░░░░░░ 41%")
elif num <= 42 :
    print ("▓▓▓▓▓▓░░░░░░░░░ 42%")
elif num <= 43 :
    print ("▓▓▓▓▓▓░░░░░░░░░ 43%")
elif num <= 44 :
    print ("▓▓▓▓▓▓▓░░░░░░░░ 44%")
elif num <= 45 : 
    print ("▓▓▓▓▓▓▓░░░░░░░░ 45%") 
elif num <= 46  : 
    print ("▓▓▓▓▓▓▓░░░░░░░░ 46%") 
elif num <= 47  : 
    print ("▓▓▓▓▓▓▓░░░░░░░░ 47%") 
elif num <= 48 : 
    print ("▓▓▓▓▓▓▓░░░░░░░░ 48%")
elif num <= 49 : 
    print ("▓▓▓▓▓▓▓░░░░░░░░ 49%") 
elif num <= 50 : 
    print ("▓▓▓▓▓▓▓▓░░░░░░░ 50%") 
elif num <= 51 : 
    print ("▓▓▓▓▓▓▓▓░░░░░░░ 51%") 
elif num <= 52 : 
    print ("▓▓▓▓▓▓▓▓░░░░░░░ 52%") 
elif num <= 53 : 
    print ("▓▓▓▓▓▓▓▓░░░░░░░ 53%") 
elif num <= 54 : 
    print ("▓▓▓▓▓▓▓▓░░░░░░░ 54%") 
elif num <= 55 : 
    print ("▓▓▓▓▓▓▓▓░░░░░░░ 55%") 
elif num <= 56 : 
    print ("▓▓▓▓▓▓▓▓░░░░░░░ 56%") 
elif num <= 57 : 
    print ("▓▓▓▓▓▓▓▓▓░░░░░░ 57%")
elif num <= 58 : 
    print ("▓▓▓▓▓▓▓▓▓░░░░░░ 58%")
elif num <= 59 : 
    print ("▓▓▓▓▓▓▓▓▓░░░░░░ 59%")
elif num <= 60 : 
    print ("▓▓▓▓▓▓▓▓▓░░░░░░ 60%")
elif num <= 61 : 
    print ("▓▓▓▓▓▓▓▓▓░░░░░░ 61%")
elif num <= 62 : 
    print ("▓▓▓▓▓▓▓▓▓░░░░░░ 62%")
elif num <= 63 : 
    print ("▓▓▓▓▓▓▓▓▓░░░░░░ 63%") 
elif num <= 64 : 
    print ("▓▓▓▓▓▓▓▓▓▓░░░░░ 64%")
elif num <= 65 : 
    print ("▓▓▓▓▓▓▓▓▓▓░░░░░ 65%")
elif num <= 66 : 
    print ("▓▓▓▓▓▓▓▓▓▓░░░░░ 66%")
elif num <= 67 : 
    print ("▓▓▓▓▓▓▓▓▓▓░░░░░ 67%")
elif num <= 68 : 
    print ("▓▓▓▓▓▓▓▓▓▓░░░░░ 68%")
elif num <= 69 : 
    print ("▓▓▓▓▓▓▓▓▓▓░░░░░ 69%")
elif num <= 70 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓░░░░ 70%")
elif num <= 71 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓░░░░ 71%")
elif num <= 72 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓░░░░ 72%")
elif num <= 73 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓░░░░ 73%")
elif num <= 74 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓░░░░ 74%")
elif num <= 75 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓░░░░ 75%")
elif num <= 76 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓░░░░ 76%")
elif num <= 77 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓░░░ 77%")
elif num <= 78 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓░░░ 79%")
elif num <= 80 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓░░░ 80%")
elif num <= 81: 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓░░░ 81%")
elif num <= 82 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓░░░ 82%")
elif num <= 83 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓░░░ 83%")
elif num <= 84 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 84%")
elif num <= 85 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 85%")
elif num <= 86 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 86%")
elif num <= 87 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 87%")
elif num <= 88 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 88%")
elif num <= 89 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 89%")
elif num <= 90 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 90%")
elif num <= 91 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 92%")
elif num <= 93 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 93%")
elif num <= 94 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 94%")
elif num <= 95 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 95%")
elif num <= 96 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 96%")
elif num <= 97 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 97%")
elif num <= 98 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 98%")
elif num <= 99 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 99%")
elif num <= 100 : 
    print ("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 100%")
else:
    print ("xxx broke my counter")

print("price:","$"+ str(amount_data))
if float(amount_data) == 10000 :
     print ("🚨🚨🚨 ", "#bitcoin is official below" )
""" the check if bitcoin is below a particular price"""
