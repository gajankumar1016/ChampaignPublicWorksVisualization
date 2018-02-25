
# import csv
# with open('all_cityworks_records.csv', "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


import csv
import pprint

def getCoordinates(keyword="flood"):
	reader = csv.DictReader(open('all_cityworks_records.csv', 'rb'))
	dict_list = []
	locations_list = []

	for line in reader:
		# print(line)
		# print("\n")
		#print(line['DESCRIPTION'].lower() + str("flood" in line['DESCRIPTION'].lower()))
		# print("\n")
		if (keyword in line['DESCRIPTION'].lower()):
			#dict_list.append(line)
			# Need to flip because x would correspond to longitude and y to latitude
			#print(line)
			if line['SRX'] and line['SRY']:
				locations_list.append({"lat":(float(line['SRX'].replace(',', ''))), "lng":(float(line['SRY'].replace(',', '')))})

	#pprint.pprint(dict_list[0]['DESCRIPTION'])
	pprint.pprint(locations_list)
	#print(len(dict_list))
	#print(len(locations_list))
	return locations_list

