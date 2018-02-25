
# import csv
# with open('all_cityworks_records.csv', "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


import csv
import pprint

def getCoordinates(keyword="flood"):
	with open('all_cityworks_records.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		#dict_list = []
		locations_list = []

		for line in reader:
			if (keyword in line['DESCRIPTION'].lower()):
				#dict_list.append(line)
				if line['SRX'] and line['SRY']:
					locations_list.append({"lat":(float(line['SRX'].replace(',', ''))), "lng":(float(line['SRY'].replace(',', '')))})

	#pprint.pprint(dict_list[0]['DESCRIPTION'])
	#pprint.pprint(locations_list)
	return locations_list

