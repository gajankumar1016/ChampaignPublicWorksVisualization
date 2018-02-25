from darksky import forecast
key = '93e9f439437303b0bc14afb340684164'
# BOSTON = key, 42.3601, -71.0589
# from datetime import datetime as dt
# t = dt(2013, 5, 6, 12).isoformat()
# boston = forecast(*BOSTON, time=t)
# print(boston.time)

CHAMPAIGN = 40.1164204, -88.2433829
SIEBEL = 40.1138028,-88.2270939
boston = forecast(key, 42.3601, -71.0589)
champaign = forecast(key, *CHAMPAIGN)
siebel = forecast(key, *SIEBEL)
#print((boston.time, boston.temperature, len(boston.hourly)))

def hourly(forecast):
	#print(forecast.hourly[1].temperature)
	return ([hour.precipProbability for hour in forecast.hourly[:10]])

hourly(siebel)


