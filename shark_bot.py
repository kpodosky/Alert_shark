import requests
import json
import tweepy
import time
from datetime import datetime

# Import keys from a separate file
from keys import bearer_token, consumer_key, consumer_secret, access_token, access_token_secret

# Constants
BTC_ATH = 69000  # Bitcoin's all-time high
UPDATE_INTERVAL = 300  # 5 minutes

def get_crypto_prices():
    """Fetch current prices for Bitcoin and Ethereum from the CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd'], data['ethereum']['usd']

def get_price_direction(current_price, previous_price):
    """Determine the price direction arrow."""
    if current_price > previous_price:
        return "⇡"
    elif current_price < previous_price:
        return "⇣"
    else:
        return "⇢"

def get_progress_bar(percentage):
    """Generate a progress bar based on the percentage."""
    filled = int(percentage / 10)
    return "⬛" * filled + "⬜" * (10 - filled)

def format_tweet(btc_price, eth_price, previous_btc_price):
    """Format the tweet content."""
    percentage = (btc_price / BTC_ATH) * 100
    direction = get_price_direction(btc_price, previous_btc_price)
    progress_bar = get_progress_bar(percentage)
    
    header = f"₿itcoin {direction}\n\n"
    body = f"{progress_bar} {percentage:.1f}%\n\n"
    footer = f"${btc_price:.2f}        ETH/BTC: {eth_price/btc_price:.5f}"
    
    return header + body + footer

def main():
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True
    )

    previous_btc_price = 0

    while True:
        try:
            btc_price, eth_price = get_crypto_prices()
            tweet_content = format_tweet(btc_price, eth_price, previous_btc_price)
            
            response = client.create_tweet(text=tweet_content)
            print(f"{datetime.now()}: {tweet_content}")
            
            previous_btc_price = btc_price
            time.sleep(UPDATE_INTERVAL)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)  # Wait a minute before retrying

if __name__ == "__main__":
    main()