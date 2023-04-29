import tweepy

consumer_key = 'MbDaxA5ch7L9EoXEM5OT1exg8'
consumer_secret = 'cbnEJa9h9SNo788qmIxZbh3TUcECBOa5F4sovehS6DzBy3derd'
access_token = '1652374140932837386-QIIsGbqGB3UcvisuYkZSnadZnEVWst'
access_token_secret = 't8opFixJ5JK5LTxoNNrrfl7Uszji2Qg2kSLJwLBzQcXhb'

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if "bahia" in status.text.lower() or "bbmp" in status.text.lower():
            try:
                api.create_friendship(status.author.id)
                print(f"Followed {status.author.name}")
            except tweepy.TweepError as e:
                print(f"Error: {e}")

    def on_error(self, status_code):
        print(f"Encountered streaming error (status code: {status_code})")
        return False  # Terminates the stream

auth = tweepy.OAuth1UserHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    token=access_token,
    token_secret=access_token_secret
)

api = tweepy.API(auth)

my_stream_listener = MyStreamListener()
my_stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)
my_stream.filter(track=['bahia', 'bbmp'])
