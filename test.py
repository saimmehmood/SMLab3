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
  
    count_result_with=[0]*7
    count_result_without=[0]*7
    r=result.get()
    for i in r:
	temp=i['tweets']
	for j in range(len(temp)):
		count_result_with[j]+=temp[j]
	temp=i['without_tweets']
	for j in range(len(temp)):
		count_result_without[j]+=temp[j]


	wth={'han':countResultWith[0],'hon':countResultWith[1],'den':countResultWith[2],'det':countResultWith[3]
         ,'denna':countResultWith[4],'denne':countResultWith[5], 'hen':countResultWith[6]}
	wthout={'han':countResultwithout[0],'hon':countResultwithout[1],'den':countResultwithout[2],
        'det':countResultwithout[3],'denna':countResultwithout[4],'denne':countResultwithout[5],
         'hen':countResultwithout[6]}
		
return jsonify({'tweets':wth, 'without_tweets': wthout})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
