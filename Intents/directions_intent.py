# /building_image.py
import requests
import json
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

# location_url = 'https://www.google.com/maps/dir/?api=1&destination='
location_url = 'https://www.google.com/maps/embed/v1/directions'
photos_url = "https://maps.googleapis.com/maps/api/place/photo"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# @app.route("/get_picture", methods=['POST'])
def get_directions(message, os):
	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good

	message = message.replace(" ", "+")

	building = message + "+UNCC"

	address = location_url + "?key=" + key + "&origin=Your+location" + "&destination=" + building

	print(address)
	return address
	
	# building = data['queryResult']['parameters']['Buildings']
	# building = building + " UNCC"

	# search_payload = {"key":key, "query":building}
	# search_req = requests.get(search_url, params=search_payload)
	# search_json = search_req.json()

	# address = search_json["results"][0]['formatted_address']
	# building = json.dumps(building)
	# address = json.dumps(address)

	# address = building + "+" + address 
	# address = address.replace(" ", "+")
	# address = address.replace('"',"")
	
	# address = location_url + address