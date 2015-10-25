from celery import Celery
import urllib
import json
import sys, os

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def count():
 result = [0,0,0,0,0,0,0]
 fileinput = urllib.urlopen("http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_19.txt")
 print "processing input"
 for line in fileinput:
        		if "han" in line:
            			result[0] += 1
       			if "hon" in line:
            			result[1] += 1
        		if "den" in line:
            			result[2] += 1
        		if "det" in line:
            			result[3] += 1
        		if "denna" in line:
            			result[4] += 1
        		if "denne" in line:
            			result[5] += 1
        		if "hen" in line:
           			result[6] += 1
 withreTweets = {'han':result[0], 'hon':result[1], 'den':result[2], 
                'det':result[3], 'denna':result[4], 'denne':result[5],
                'hen':result[6]}

 print len(result)
 return withreTweets
