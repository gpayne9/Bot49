# /index.py
import os
import dialogflow
import requests
import json
import pusher
import imghdr
from Intents.picture_intent import get_building_image
from Intents.directions_intent import get_directions
from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

def detect_intent_texts(project_id, session_id, text, language_code):
	session_client = dialogflow.SessionsClient()
	session = session_client.session_path(project_id, session_id)
	
	if text:
		text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
		query_input = dialogflow.types.QueryInput(text=text_input)
		response = session_client.detect_intent(session=session, query_input=query_input)
		print(response)
		# Send a JSON object that holds the message from Dialog-Flow and intent name 
		message = {"message": response.query_result.fulfillment_text, "intent": response.query_result.intent.display_name}
													
		return message

@app.route('/send_message', methods=['POST'])
def send_message():
	message = request.form['message']
	project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
	fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
	#response_text = { "message":  fulfillment_text }
	# print(fulfillment_text)	# Print response text
	return jsonify(fulfillment_text) 

# function 
@app.route("/bot_49", methods=['POST'])
def results():#detect intent

	data = request.get_json(silent=True) # get data in json form 
	print(data)
	#if(data['intent'] == picture)	
	#else if (data['intent'] == directions)
	intent = data['queryResult']['intent']['displayName']
	print(data['queryResult']['intent']['displayName'])
	if(intent == 'Pictures'):				
		response = get_building_image(data, os)
	elif(intent == 'Directions'):
		response = get_directions(data,os)
	print(response)
	
	reply = {
		"fulfillmentText": response,
	}
	return jsonify(reply)

# run Flask app 
if __name__ == "__main__":
	app.run()
