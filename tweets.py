from celery import Celery
import urllib
import json
import sys, os

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def count():
 result = [0,0,0,0,0,0,0]
 resultWithout = [0,0,0,0,0,0,0]
 fileinput = urllib.urlopen("http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_19.txt")
 print "processing input"
 for line in fileinput:
     if line != "\n":
        work = json.loads(line)
        if "han" in work['text']:
                result[0] += 1
                if "retweeted_status" in work.viewkeys():
                    resultWithout[0] += 1
        if "hon" in work['text']:
                result[1] += 1
                if "retweeted_status" in work.viewkeys():
                    resultWithout[1] += 1
        if "den" in work['text']:
                result[2] += 1
                if "retweeted_status" in work.viewkeys():
                    resultWithout[2] += 1
        if "det" in work['text']:
                result[3] += 1
                if "retweeted_status" in work.viewkeys():
                    resultWithout[3] += 1
        if "denna" in work['text']:
                result[4] += 1
                if "retweeted_status" in work.viewkeys():
                    resultWithout[4] += 1
        if "denne" in work['text']:
                result[5] += 1
                if "retweeted_status" in work.viewkeys():
                    resultWithout[5] += 1
        if "hen" in work['text']:
                result[6] += 1
                if "retweeted_status" in work.viewkeys():
                    resultWithout[6] += 1

 withreTweets = {result[0], result[1], result[2],
                result[3], result[4], result[5],
                result[6]}
 withoutTweets = {resultWithout[0], resultWithout[1], resultWithout[2],
                resultWithout[3], resultWithout[4], resultWithout[5],
                resultWithout[6]}

 print len(result)
 return ({'tweets':withreTweets, 'without_tweets':withoutTweets})
