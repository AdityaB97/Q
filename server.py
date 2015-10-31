from flask import Flask, request, render_template
app = Flask(__name__)

queue = []

@app.route("/")
def hello():
	return app.send_static_file('index.html')

@app.route("/api/info", methods=["POST"])
def receive_client():
	name = request.form['name']
	email = request.form['email']
	event_id = request.form['event_id']
	queue.append([name, email, event_id])
	print(queue)
	return "Thank you. Your response has been recorded."

@app.route("/data")
def show_queue():
	return render_template("queue.html", queue=queue)

if __name__ == "__main__":
	app.run(debug=True)