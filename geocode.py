import httplib2
import json

def getGeocodeLocation(inputString):
	google_api_key = "PASTE_YOUR_KEY_HERE"
	locationString = inputString.replace(" ","+")
	url = ('http://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString, google_api_key))
	h = httplib2.Http()
	response, content = h.request(url,'GET')
	result = json.loads(content)
	return result