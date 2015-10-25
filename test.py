from flask import Flask, jsonify
import subprocess
import sys
import tweets as twt

app = Flask(__name__)


@app.route('/count/api/v1.0/saysomething', methods=['GET'])
def cow_say():
    data=twt.count.delay()
    #print len(data)
    
    return jsonify(data.get()) 

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
