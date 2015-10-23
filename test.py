from flask import Flask, jsonify
import subprocess
import sys
import tweets as twt

app = Flask(__name__)


@app.route('/count/api/v1.0/saysomething', methods=['GET', 'POST'])
def cow_say():
    data=twt.count()
    print len(data)
    han, hon, den, det, denna, denne, hen = data
    return (han, hon, den, det, denna, denne, hen)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
