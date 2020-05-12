import geojson

def convert(geojson):
	return geojson



def get_coordinates(data):
	ll = []
	for feature in data['features']:
			#print(feature['geometry']['type'])
			ll.append( [ el for el  in feature['geometry']['coordinates']])
			##print("\r\n")
	return ll
	

def make_line_from_coord_list(list_of_lists, param1="_", param2="_"):
	for list in list_of_lists:
		print(str(list[0])+";"+str(list[1]) + ";" + str(param1) + "_"+ str(param2))
	print("\n\r")


#def get_high(data, object_id):
#   try / catch
#	return data["features"][object_id]['properties']["BLDG_H"]

def get_line(data, object_id):
	pass
#	return "\n".join([  (str(elem) for elem in get_coordinates(data, object_id=1) ])



for feature in data['features']:
#	make_line_from_coord_list(feature['geometry']['coordinates'][0][0], feature['properties']['addr:street'], feature['properties']['addr:housenumber'])  ### uwaga na multi polygony

	make_line_from_coord_list(feature['geometry']['coordinates'][0])  ### uwaga na multi polygony no i nie bedzie dzialac dla linii!!

##make_line_from_coord_list(feature['geometry']['coordinates'][0][0])  ## polygond
##make_line_from_coord_list(feature['geometry']['coordinates'][0])  #lines
##make_line_from_coord_list([feature['geometry']['coordinates']])  #points
