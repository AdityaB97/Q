import flask
from twilio.rest import TwilioRestClient
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST"])
def send_message():
	phone_number = request.form.get('phone_number')
	message = request.form.get('message')
 
	ACCOUNT_SID = "AC8463c9cf9bee23b138a7aa6fcece2d82" # old: "ACfdea28b27b6aade7a9277dcb59c9ecdb" 
	AUTH_TOKEN = "7b762b4d98ba3e30a69bf11985d15083" # old: "0a171e4be02bd256d1122f32303608f7" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

	client.messages.create(
		to=phone_number, 
		from_="+14242773397", # old: "+14243284604" 
		body=message,  
	)

	resp = flask.Response("success")
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp
	

if __name__ == "__main__":
	app.run(debug=True)