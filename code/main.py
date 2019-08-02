# importing the module
import btcapi
import settings
import time
import tweepy


def main():
    '''
    Main workhorse of the script
    :return:
    '''

    # tweeter authentication
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)

    api = tweepy.API(auth)

    # fetch current price from provider
    current_btc_price = btcapi.get_current_price()
    ath = btcapi.ATH

    # calculate live progress
    live_progress = (current_btc_price/ath) * 100

    # create tweet from live_progress data
    tweet = settings.tweet_text_format%(live_progress)

    # update tweeter status
    api.update_status(status=tweet)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(settings.post_frequency_in_secs)