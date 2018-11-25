# /index.py
import os
import dialogflow
import requests
import json
import pusher
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
from Intents import picture_intent
from Intents import directions_intent
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/favicon.ico') 
def favicon(): 
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='images/favicon.png')

# Function in charge of parsing the intent information from Dialog-Flow
def detect_intent_texts(project_id, session_id, text, language_code):
	session_client = dialogflow.SessionsClient()
	session = session_client.session_path(project_id, session_id)
	
	if text:
		text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
		query_input = dialogflow.types.QueryInput(text=text_input)
		response = session_client.detect_intent(session=session, query_input=query_input)

		# Send a JSON object that holds the message from Dialog-Flow and intent name 
		message = {"message": response.query_result.fulfillment_text, "intent": response.query_result.intent.display_name}
													
		return message

# Function in charge of sending and recieving messages from Dialog-Flow
@app.route('/send_message', methods=['POST'])
def send_message():
	message = request.form['message']
	project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
	fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
	# response_text = { "message":  fulfillment_text}

	return jsonify(fulfillment_text)

# function
@app.route("/bot_49", methods=['POST'])
def results():
	message = request.form['message']
	intent = request.form['intent']
	# data = request.get_json(silent=True) # get data in json form
	# intent = data['queryResult']['intent']['displayName']
	print("hi")
	if(intent == 'pictures'):
		# response = picture_intent.get_building_image(data, os)
		response = picture_intent.get_building_image(message, os)
	elif(intent == 'directions'):
		# response = directions_intent.get_directions(data, os)
		response = directions_intent.get_directions(message, os)
		response = {"fulfillmentText": response}

	return jsonify(response)

# function
@app.route("/send_results", methods=['GET'])
def post_results(response):
	return response

# run Flask app
if __name__ == "__main__":
	app.run(debug=True)
