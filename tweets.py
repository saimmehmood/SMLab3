from flask import Flask, jsonify
from celery import Celery
import subprocess
import sys
import urllib


app = Flask(__name__)

@app.route('/tweets/api/v1.0/saysomething', methods=['GET'])
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
	data=subprocess.check_output(
	[
	print ("han -",han)
	print ("hon -",hon)
	print ("den -",den)
	print ("det -",det)
	print ("denna -",denna)
	print ("denne -",denne)
	print ("hen -",hen) ]
	)
	return data
	
if __name__ == '__main__':

    app.run(host='0.0.0.0',debug=True)
    
