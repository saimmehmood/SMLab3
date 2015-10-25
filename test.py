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
    arr = [0,0,0,0,0,0,0]
    jobs.append(twt.count)
    my_task = group(jobs)
    result = my_task.apply_async()
  
    count_result_with=[0]*7
    count_result_without=[0]*7
    r=result.get()
    for i in r:
	temp=i['tweets']
	for j in range(len(temp)):
		arr[j]+=temp[j]
	temp=i['without_tweets']
	for j in range(len(temp)):
		arr[j]+=temp[j]


	wth={'han':arr[0],'hon':arr[1],'den':arr[2],'det':arr[3]
         ,'denna':arr[4],'denne':arr[5], 'hen':arr[6]}
	wthout={'han':arr[0],'hon':arr[1],'den':arr[2],
        'det':arr[3],'denna':arr[4],'denne':arr[5],
         'hen':arr[6]}
		
return jsonify({'tweets':wth, 'without_tweets': wthout})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
