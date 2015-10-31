# Q - You'll never have to stand in line again!

Q is an online queue management system. Organizers can create queues for their events. Instead of waiting in line, people 
can register themselves in a virtual queue. This delocalizes the waiting process and allows people to be productive in the time
that they would otherwise spend waiting. This gives organizers great flexibility in using Q. One can set up queues for anything from 
food distribution to doctor's appointments.

In the backend, the queues are represented by lists of users in JavaScript. Each user is itself a list of variables representing attributes such as 
name, contact details, etc. The organizers have access to an interface with 2 options: "add" and "next". "Add" adds a person to the queue, 
"next is used to periodically updating the queue by "popping" the first user out of the list when they reach the front. The organizer interface
is a simple HTML form, with "add and "next" being the submission options.

Users interact with the queue through text messages on their mobile phones. After being added to the queue through the organizer's form, each user is periodically
updated about their status in the queue (this happens each time the organizer presses "next"). Users are also notified when they reach the
front of the line. In the next update, I plan to give users the capacity to add and remove themselves from the queue by text message. Users
will also have the capacity to report delays, and adjust their queue position accordingly

All the messaging action occurs thorugh a Python script hosted on localhost, driven by the Twilio messaging API. Whenever "next" is triggered
by an organizer, an AJAX request is sent to the Python script, which then performs the task of messaging. The queue is
currently stored in the JavaScript of the organizer page, and will be given a dedicated database in future scale-ups. 

All of the code for this project was written during the CSUA Hackathon 2015.

- A project by Aditya Baradwaj