from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACfdea28b27b6aade7a9277dcb59c9ecdb" 
AUTH_TOKEN = "[AuthToken]" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+13106621364", 
	from_="+14243284604", 
	body="testing",  
)