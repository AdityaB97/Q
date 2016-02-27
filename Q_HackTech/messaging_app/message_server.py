import flask
from twilio.rest import TwilioRestClient
from flask import Flask, request, render_template, redirect
import twilio.twiml
from collections import deque

# app = Flask(__name__)

class Person:
	def __init__(self, name, number):
		self.name = name
		self.number = number

class Database:
	def __init__(self):
		self.q = []
		self.q_dict = {}

	# Takes in a Person object and adds it to the database
	def add(self, person):
		self.q.append(person)
		self.q_dict[person.number] = person
		person.index = len(self.q) - 1 

	def update_indices(self):
		for i in range(len(self.q)):
			person = self.q[i]
			person.index = i

	def pop_first(self):
		number = self.q[0].number
		return self.remove(number)

	def remove(self, number):
		person = self.q_dict[number]
		index = person.index
		del self.q[index]
		del self.q_dict[number]
		self.update_indices()
		return person

	def lookup(self, number):
		return self.q_dict[number]

	def exists(self, number):
		return number in self.q_dict

def print_all(database):
	for person in database.q:
		print(person.name, person.number)

person1 = Person("Person1", "1")
person2 = Person("Person2", "2")
person3 = Person("Person3", "3")
person4 = Person("Person4", "4")
person5 = Person("Person5", "5")

database = Database()
database.add(person1)
database.add(person2)
database.add(person3)
database.add(person4)
database.add(person5)


# @app.route("/", methods=["POST"])
# def send_message():
# 	phone_number = request.form.get('phone_number')
# 	message = request.form.get('message')
 
# 	ACCOUNT_SID = "AC8463c9cf9bee23b138a7aa6fcece2d82" # old: "ACfdea28b27b6aade7a9277dcb59c9ecdb" 
# 	AUTH_TOKEN = "7b762b4d98ba3e30a69bf11985d15083" # old: "0a171e4be02bd256d1122f32303608f7" 
	 
# 	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

# 	client.messages.create(
# 		to=phone_number, 
# 		from_="+14242773397", # old: "+14243284604" 
# 		body=message,  
# 	)

# 	resp = flask.Response("success")
# 	resp.headers['Access-Control-Allow-Origin'] = '*'
# 	return resp

callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+13106621364": "Aditya",
    "+18136009605": "Jordan",
}

# @app.route("/", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond and greet the caller by name."""
 
#     from_number = request.values.get('From', None)
#     body = request.values.get('Body', None)

#     if not database.exists(from_number):

 	
#     message = message + " \n Your body: " + body
#     resp = twilio.twiml.Response()
#     resp.message(message)
 
#     return str(resp)

# if __name__ == "__main__":
# 	app.run(debug=True)