# /index.py
import os
import dialogflow
import requests
import json
import pusher
import imghdr
import building_image as building_image # building_image.py
from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

photos_url = "https://maps.googleapis.com/maps/api/place/photo"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

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
													
		return response.query_result.fulfillment_text

@app.route('/send_message', methods=['POST'])
def send_message():
	message = request.form['message']
	project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
	fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
	response_text = { "message":  fulfillment_text }
	# print(fulfillment_text)	# Print response text
	return jsonify(response_text)

# function 
@app.route("/bot_49", methods=['POST'])
def results():
	data = request.get_json(silent=True) # get data in json form 
	building = data['queryResult']['parameters']['Buildings']
	building = building + " UNCC"
	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good		

	bi = building_image.get_building_image(key, building, search_url, photos_url)

	return bi

# run Flask app
if __name__ == "__main__":
	app.run()
