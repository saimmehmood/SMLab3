from flask import Flask, jsonify
from celery import Celery
import urllib
app = Celery('tasks', backend='amqp', broker='amqp://')

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
@app.route('/tweets/api/v1.0/saysomething', methods=['GET'])
@celery.task
def count():
	han = hon = den = det = denna = denne = hen = 0;
	fileinput = urllib.urlopen("http://smog.uppmax.uu.se:8080/swift/v1/tweets/tweets_19.txt")
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
