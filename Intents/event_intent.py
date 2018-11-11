# /building_image.py
import requests
import json
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

#Matt and Meghana and Mehmet
#data
# @app.route("/get_picture", methods=['POST'])
def get_events(data):
	
	#Parse data


	#scrape events from https://campusevents.uncc.edu/
	

	#format response

	