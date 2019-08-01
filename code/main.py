# importing the module
import btcapi
import settings
import tweepy

def main():
    # authentication
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)

    api = tweepy.API(auth)

    current_btc_price = btcapi.get_current_price()
    ath = btcapi.ATH
    live_progress = (current_btc_price/ath) * 100

    tweet = settings.tweet_text_format%(live_progress)

    api.update_status(status=tweet)

if __name__ == '__main__':
    while True:
        main()