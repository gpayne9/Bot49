# /building_image.py
import requests
import json
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

# @app.route("/get_picture", methods=['POST'])
def get_building_image(key, building, search_url, photos_url):

	search_payload = {"key":key, "query":building}
	search_req = requests.get(search_url, params=search_payload)
	search_json = search_req.json()
	print(search_json) # Gives me the entire payload for a building at UNCC

	photo_id = search_json["results"]
	photo_id = search_json["results"][0]["photos"][0]["photo_reference"]

	photo_payload = {"key" : key, "maxwidth" : 500, "maxwidth" : 500, "photoreference" : photo_id}
	photo_request = requests.get(photos_url, params=photo_payload)
	print(photo_payload)
	print(photo_request)

	photo_type = imghdr.what("", photo_request.content)
	photo_name = "static/" + building + "." + photo_type

	with open(photo_name, "wb") as photo:
		photo.write(photo_request.content)

	print(photo_name)
	return send_from_directory('.', photo_name)
	# return '<img src='+ photo_name + '>'

