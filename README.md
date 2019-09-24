# Year Progress Twitter Bot in Python

Hi, I'm [@kilanko](https://twitter.com/paulkilanko) building a twitter bot in python to achieve this (https://twitter.com/Alert_Shark)

# What does this twitter bot?
This bot post bitcoin price Progress in percents in a tweet.

## Installation


## Connecting to Twitter

At this point you need to register a Twitter account and also get its "app info".

So create a Twitter account for whatever account you want to tweet this stuff. Twitter doesn't allow you to register multiple twitter accounts on the same email address. I recommend you create a brand new email address (perhaps using Gmail) for the Twitter account. Once you register the account to that email address, wait for the confirmation email. Then go here and log in as the Twitter account for your bot:

https://apps.twitter.com/app/new

Once you're there, fill in the required fields: name, description, website. None of it really matters at all to your actual app, it's just for Twitter's information. Do the captcha and submit.

Next you'll see a screen with a "Details" tab. Click on the "Settings" tab and under "Application Type" choose "Read and Write", then hit the update button at the bottom.

Then go to the Keys and Access Tokens tab, and at the bottom click "create my access token". Nothing might happen immediately. Wait a minute and reload the page. then there should be "access token" and "access token secret", which are both long strings of letters and numbers.

Now use a text editor to open up the "config.js" file. It should look like this:

```javascript
module.exports = {
  consumer_key:         'YourCusumerkey',
  consumer_secret:      'YourSecretKey',
  access_token:         'YourAccessKey',
  access_token_secret:  'YourAccessSecret'
}
```

In between those quotes, paste the appropriate info from the Details page. This is essentially the login information for the app.



