from flask import Flask, render_template, json
from test_darksky import hourly
from darksky import forecast
from citydata import getCoordinates
from apikeys import MAPS_API_KEY

app = Flask(__name__)

SIEBEL_LAT = 40.1138028
SIEBEL_LNG = -88.2270939
SIEBEL = SIEBEL_LAT, SIEBEL_LNG

@app.route("/", methods=['GET', 'POST'])
def hello():
	#return "<b>" + str(hourly(siebel)) + "</b>"
	lat = SIEBEL_LAT
	lng = SIEBEL_LNG
	origLocations = getCoordinates()
	return render_template('clusters.html', MAPS_API_KEY=MAPS_API_KEY, lat=lat, lng=lng, origLocations=json.dumps(origLocations))

if __name__ == "__main__":
	app.run(debug=True)