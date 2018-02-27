# ChampaignPublicWorksVisualization

This is our HackIllinois 2018 project to visualize public works data (i.e. pothole repairs, plow requests, flood calls, etc.) in the City of Champaign from 2009 to 2017.

The app was written using Flask and Marker Clustering with Google Maps and provides a way to visualize the data in the csv file provided by the City of Champaign. The user can select a particular kind of public works request and then view which areas of Champaign had the highest frequency of that particular kind of request. Upon clicking a specific cluster, the map will zoom in and re-cluster the locations.

Future steps would include a feature to allow users to filter the data by year and integration with sensors and realtime weather reports.

To run, you will need to provide an API key for the Google Maps Javascript API. First, clone the repository and create a file called apikeys.py in the main folder. Add the following line to the file:
MAPS_API_KEY = "Insert Your Google Maps API Here"

You can then run "python app.py" from a terminal.

The project modified and added upon the following tutorial for Marker Clustering with the Google Maps Javascript API:
https://developers.google.com/maps/documentation/javascript/marker-clustering

Contact:
Gajan Kumar: gajankumar1016@gmail.com
Kit Ng: kitn@umich.edu
Ben Huemann: bhuemann@purdue.edu
Arin Mauk: arin.mauk7@gmail.com
Aganze Mihigo: amihigo2@illinois.edu
