import flask
from flask import Flask, request, render_template
import smtplib
app = Flask(__name__)

queue = []

@app.route("/", methods=["POST"])
def send_email():
	email = request.form.get('email')
	message = request.form.get('message')

	fromaddr = 'qmessaging@gmail.com'
	toaddrs  = email
	msg = "\r\n".join([
	  "From: qmessaging@gmail.com",
	  "To: "+email,
	  "Subject: Queue update!",
	  "",
	  message
	  ])
	username = 'qmessaging@gmail.com'
	password = 'csuahackathon'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

	resp = flask.Response("success")
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

if __name__ == "__main__":
	app.run(debug=True)