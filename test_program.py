from flask import Flask, jsonify
import subprocess
import sys
import time 
import tweets as twt


def test_program():
    print "Starting Process"
		new_task = twt.count.delay()

		while(new_task.status != 'SUCCESS'):
			time.sleep(10)
			print (new_task.status)
			print "Waiting for the task to complete"

		os.system('python flask_example.py ' + sys.argv[1])


if __name__ == '__main__':
	test_program()
