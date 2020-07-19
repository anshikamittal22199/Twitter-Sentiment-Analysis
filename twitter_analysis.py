
import string

from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('donald trump') \
        .setSince("2019-08-01") \
        .setUntil("2020-09-28") \
        .setMaxTweets(1000)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets=[[tweet.text] for tweet in tweets]
    return text_tweets



text=""
text_tweets=get_tweets()
length=len(text_tweets)

for i in range(0,length):
    text=text_tweets[i][0] + " " + text


lower_case=text.lower();
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")



final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):

        final_words.append(word)

emotion_list=[]
with open("emotions.txt",'r') as file:
    for line in file:
        clear_line = line.replace("\n","").replace(",","").replace("'","").strip()

        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w=Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral vibe")


sentiment_analyse(cleaned_text)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
