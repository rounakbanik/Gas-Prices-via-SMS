# -*- coding: utf-8 -*-
import os
from flask import Flask, request
from twilio.rest import Client
import json

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC705c0140161dcf44f53e96e40fc492cc'
auth_token = 'e3cb4c9dd7b1f2a80f26a3e24779ebd6'
client = Client(account_sid, auth_token)


app = Flask(__name__)
app.debug = True
queue = []

@app.route('/', methods=['POST', 'GET'])
def request_handler():
	if request.method == 'POST':
		print("Received a notification from the webhook!")
		data = (request.json)
		# if len(data['event']['activity'])==1:
		# 	timestamp = data['createdAt']
		# 	from_address = data['event']['activity'][0]['fromAddress']
		# 	to_address = data['event']['activity'][0]['toAddress']
		# 	blockNum =  data['event']['activity'][0]['blockNum']
		# 	hash =  data['event']['activity'][0]['hash']


		# else:
		# 	for i in range(len(data['event']['activity'])):
		# 		timestamp = data['createdAt']
		# 		from_address = data['event']['activity'][i]['fromAddress']
		# 		to_address = data['event']['activity'][i]['toAddress']
		# 		blockNum =  data['event']['activity'][i]['blockNum']
		# 		hash =  data['event']['activity'][i]['hash']


		print("DATA: ", data)


		message = client.messages.create(body='Gas prices have dropped below 50 Gwei!' ,from_='+18149956820', to='+918439860325')

		print(message.sid)


	return ("Server is up!")

def run():
	app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
