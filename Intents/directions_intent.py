# /building_image.py
import requests
import json
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)
location_url = 'https://www.google.com/maps/dir/?api=1&destination='
photos_url = "https://maps.googleapis.com/maps/api/place/photo"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
#Guy and Lauren
# @app.route("/get_picture", methods=['POST'])
def get_directions(data,os):
	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good

	#parse payload(data)
	building = data['queryResult']['parameters']['Buildings']
	building = building + " UNCC"

	#google stuff(key, building)

	search_payload = {"key":key, "query":building}
	search_req = requests.get(search_url, params=search_payload)
	search_json = search_req.json()
	print(search_json)
	address = search_json["results"][0]['formatted_address']
	print(address)
	building = json.dumps(building)
	address = json.dumps(address)
	address = building + "+" + address #https://www.google.com/maps/dir/?api=1&destination=Denny+Hall+UNCC9125+Mary+Alexander+Rd,+Charlotte,+NC+28262,+USA
	address = address.replace(" ", "+")
	address = address.replace('"',"")
	
	address = location_url + address
	print(address)
	return address

	