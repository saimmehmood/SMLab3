#!flask/bin/python
from flask import Flask, jsonify
from celery import Celery
import urllib
import subprocess
import sys

app = Flask(__name__)
app = Celery('tasks', backend='amqp', broker='amqp://')

@app.route('/tweets/api/v1.0/count', methods=['GET'])

@app.task
def print_hello():
    print 'hello there'
@app.task
def count():
	han = hon = den = det = denna = denne = hen = 0;
	for i in range(0, 20):
		fileinput = urllib.urlopen("http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_"+str(i)+".txt")
		for line in fileinput:
			if "han" in line:
		    		han += 1
		       	if "hon" in line:
		    		hon += 1
			if "den" in line:
		    		den += 1
			if "det" in line:
		    		det += 1
			if "denna" in line:
		    		denna += 1
			if "denne" in line:
		    		denne += 1
			if "hen" in line:
		   		hen += 1
		   			
	print ("han -",han)
	print ("hon -",hon)
	print ("den -",den)
	print ("det -",det)
	print ("denna -",denna)
	print ("denne -",denne)
	print ("hen -",hen)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
    
