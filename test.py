from flask import Flask, jsonify
import subprocess
import sys
import tweets as twt
import json
from celery import group

app = Flask(__name__)


@app.route('/count/api/v1.0/saysomething', methods=['GET'])
def cow_say():
    jobs=[]

    jobs.append(twt.count.delay())
    my_task = group(jobs)
    result = my_task.apply_async()
    
    r = result.get()
    
    for i in r:
    	with_tweet = i['tweets']
	without = i['without_tweet']
    #print len(data)
    
    return jsonify({'tweet':with_tweet, 'retweet':without}) 

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
