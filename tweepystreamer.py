from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


# # # # TWITTER STREAMER # # # #
class StreamerTwitter():


    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets):
        self.fetched_tweets= fetched_tweets

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets, 'a') as ts:
                ts.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.
    topic_list = ["Narendra Modi", "Covid19", "India", "Indian Army"]
    fetched_tweets = "tweetanalyse.txt"

    streamer_twitter = StreamerTwitter()
    streamer_twitter.stream_tweets(fetched_tweets, topic_list)