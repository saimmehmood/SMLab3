from flask import Flask, jsonify
import subprocess
import sys
import worker_code as twt
import json
from celery import group

app = Flask(__name__)


@app.route('/count/api/v1.0/saysomething', methods=['GET'])
def cow_say():
    jobs=[]
    arr1 = [0,0,0,0,0,0,0]
    arr2 = [0,0,0,0,0,0,0]
    jobs.append(twt.count)
    my_task = group(jobs)
    result = my_task.apply_async()
  
    count_result_with=[0]*7
    count_result_without=[0]*7
    r=result.get()
    for i in r:
	temp=i['tweets']
	for j in range(len(temp)):
		arr1[j]+=temp[j]
	temp=i['without_tweets']
	for j in range(len(temp)):
		arr2[j]+=temp[j]


	wth={'han':arr1[0],'hon':arr1[1],'den':arr1[2],'det':arr1[3]
         ,'denna':arr1[4],'denne':arr1[5], 'hen':arr1[6]}
	wthout={'han':arr2[0],'hon':arr2[1],'den':arr2[2],
        'det':arr2[3],'denna':arr2[4],'denne':arr2[5],
         'hen':arr2[6]}
		
return jsonify({'tweets':wth, 'without_tweets': wthout})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
