import tweepy


# API key: k1WvBCOCjvk6Nv6Drnjmh85Eb
# API Secret: 79nNKRFkzHp7dLL13zCNpbtdCpv7Hdo7WLwrmWpRJ8jzuauRMG
# bearer token: AAAAAAAAAAAAAAAAAAAAALb%2FKQEAAAAARIOFPUtXdF8GzWHWQYeeOXhHwlw%3DKpLeMtd4aQrnhZ5bqFBKvRvNRZw4MMePzr8ZiZNvBO263ijTwD
# access token: 1155475370914828289-mD8YDbn9UeNeC6BjA2y1PMKk3zzkYr
# access token secret: MQdq9xYokO5b1F7DM1Ewcmg0KLmtGGfUsMCAbFGF3Uhri

auth = tweepy.OAuthHandler("1155475370914828289-mD8YDbn9UeNeC6BjA2y1PMKk3zzkYr", "79nNKRFkzHp7dLL13zCNpbtdCpv7Hdo7WLwrmWpRJ8jzuauRMG")
auth.set_access_token("1155475370914828289-mD8YDbn9UeNeC6BjA2y1PMKk3zzkYr", "MQdq9xYokO5b1F7DM1Ewcmg0KLmtGGfUsMCAbFGF3Uhri")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)