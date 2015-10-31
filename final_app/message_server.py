import flask
from twilio.rest import TwilioRestClient
from flask import Flask, request, render_template

app = Flask(__name__)

queue = []

@app.route("/")
def main_file():
	return app.send_static_file('index.html')


@app.route("/message", methods=["POST"])
def send_message():
	phone_number = request.form.get('phone_number')
	message = request.form.get('message')
 
	ACCOUNT_SID = "ACfdea28b27b6aade7a9277dcb59c9ecdb" 
	AUTH_TOKEN = "[AuthToken]" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

	client.messages.create(
		to=phone_number, 
		from_="+14243284604", 
		body=message,  
	)

	resp = flask.Response("success")
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp
	

if __name__ == "__main__":
	app.run(debug=True)