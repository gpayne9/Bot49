# /building_image.py
import requests
import json
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)
#faith and Kate
photos_url = "https://maps.googleapis.com/maps/api/place/photo"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
#data
# @app.route("/get_picture", methods=['POST'])
def get_building_image(data, os):
	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good

	#parse payload(data)
	building = data['queryResult']['parameters']['Buildings']
	building = building + " UNCC"

	#google stuff(key, building)
	
	search_payload = {"key":key, "query":building}
	search_req = requests.get(search_url, params=search_payload)
	search_json = search_req.json()
	# print(search_json) # Gives me the entire payload for a building at UNCC

	photo_id = search_json["results"]
	photo_id = search_json["results"][0]["photos"][0]["photo_reference"]

	photo_payload = {"key" : key, "maxwidth" : 500, "maxwidth" : 500, "photoreference" : photo_id}
	photo_request = requests.get(photos_url, params=photo_payload)

	photo_type = imghdr.what("", photo_request.content)
	photo_name = "imgs/" + building + "." + photo_type

	with open(photo_name, "wb") as photo:
		photo.write(photo_request.content)

	print(photo_name)

	# return send_from_directory('.', photo_name)
	return '<img src=' + photo_name + '>'


	