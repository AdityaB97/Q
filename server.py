from flask import Flask, request, render_template
app = Flask(__name__)

queue = []

@app.route("/")
def hello():
	return app.send_static_file('index.html')

@app.route("/api/info", methods=["POST"])
def receive_client():
	name = request.form['name']
	area_code = request.form['area_code']
	phone_number = request.form['phone_number']
	event_id = request.form['event_id']
	event_name = request.form['event_name']
	queue.append([name, area_code, phone_number, event_id, event_name,])
	print(queue)
	return "Thank you. Your response has been recorded."

@app.route("/data")
def show_queue():
	return render_template("queue.html", queue=queue)

if __name__ == "__main__":
	app.run(debug=True)