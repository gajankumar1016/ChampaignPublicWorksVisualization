from flask import Flask, render_template, json, request
from test_darksky import hourly
from darksky import forecast
from citydata import getCoordinates
from apikeys import MAPS_API_KEY

app = Flask(__name__)

SIEBEL_LAT = 40.1138028
SIEBEL_LNG = -88.2270939
SIEBEL = SIEBEL_LAT, SIEBEL_LNG

@app.route("/", methods=['GET', 'POST'])
def index():
	#The map will be centered at the coordinates for the Siebel Center
	lat = SIEBEL_LAT
	lng = SIEBEL_LNG

	if request.method == 'POST':
		type_of_work = request.form['citywork'];
		origLocations = getCoordinates(type_of_work)
		return render_template('clusters.html', MAPS_API_KEY=MAPS_API_KEY, lat=lat, lng=lng, origLocations=json.dumps(origLocations), type_of_work=type_of_work)

	else:
		#Get coordinates for default value
		origLocations = getCoordinates("flood")
		return render_template('clusters.html', MAPS_API_KEY=MAPS_API_KEY, lat=lat, lng=lng, origLocations=json.dumps(origLocations), type_of_work="flood")

if __name__ == "__main__":
	app.run()