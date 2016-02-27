from collections import deque
from twilio.rest import TwilioRestClient
import flask
from flask import Flask, request, render_template

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

Q = deque()

app = Flask(__name__)

def send_message():
	phone_number = request.form.get('phone_number')
	message = request.form.get('message')
 
	ACCOUNT_SID = "ACfdea28b27b6aade7a9277dcb59c9ecdb" 
	AUTH_TOKEN = "0a171e4be02bd256d1122f32303608f7" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

	client.messages.create(
		to= phone_number, 
		from_="+14243284604", 
		body=message,  
	)

	resp = flask.Response("success")
	return resp
	

if __name__ == "__main__":
	app.run(debug=True)
