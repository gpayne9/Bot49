# /picture_intent.py
import requests
import json
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

photos_url = "https://maps.googleapis.com/maps/api/place/photo"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# @app.route("/get_picture", methods=['POST'])
@app.route("/sendRequest/<string:query>")
def get_building_image(message, os):

	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good
	building = message + " UNC Charlotte"

	search_payload = {"key":key, "query":building}
	search_req = requests.get(search_url, params=search_payload)
	search_json = search_req.json()

	photo_id = search_json["results"]
	photo_id = search_json["results"][0]["photos"][0]["photo_reference"]

	photo_payload = {"key" : key, "maxwidth" : 500, "maxwidth" : 500, "photoreference" : photo_id}
	photo_request = requests.get(photos_url, params=photo_payload)

	picture_url = (photos_url + "?maxwidth=500" + "&photoreference=" + photo_id + "&key=" + key)
	
	return picture_url

