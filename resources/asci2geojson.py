
import re
import geojson

path_to_file="LN_izoline.TXT"
path_to_geojson = "LN_izoline_TXT.geojson"
file_lines=[]

with open(path_to_file) as file:
    file_lines=file.readlines()


#print([el for el in file_lines if re.match(r'^IsoValue.*$', el)])

isoline_value=0
isoline_coords_tmp=[]
features = []

for line in file_lines:
    match_isoline_start=re.search(r'^(IsoValue)\s*([0-9]+)\s*(.*)\s*$', line)   ##te regexy mozna budowac wczesniej
    match_coords=re.search(r'^([0-9]+\,[0-9]+);([0-9]+\,[0-9]+);(.*)\s*$', line)  #to samo

    if match_isoline_start:
        if isoline_value and isoline_coords_tmp :  ##jezeli juz cos bylo - to zrob dumpa
            ls = geojson.LineString(coordinates = isoline_coords_tmp)
            features.append(geojson.Feature(geometry=ls, properties={"value": isoline_value}))

            isoline_coords_tmp = []   ##i wyczysc temporary izolinie
            isoline_value=match_isoline_start.group(2)  ## a do wartosci wrzuc obecna
            ls = None

    elif match_coords:
        isoline_coords_tmp.append((
                float(match_coords.group(1).replace(',', '.')),
                float(match_coords.group(2).replace(',', '.')),
                ))

ls = geojson.MultiLineString(coordinates = isoline_coords_tmp)
features.append(geojson.Feature(geometry=ls, properties={"value": isoline_value}))


#feature_collection = geojson.FeatureCollection(features)

with open(path_to_geojson, 'w') as file:
    for f in features:
        geojson.dump(f, file)



##feature_collection = geojson.FeatureCollection(features)


#print(features)
#print(isoline_coords[3])
#print(isoline_coords[4])



##slownik --- { 40 : [ lista tupli ze wspolrzednymi]}


##>>> from geojson import LineString

##>>> LineString([(8.919, 44.4074), (8.923, 44.4075)])  ---- lista tupli!!
##{"coordinates": [[8.91..., 44.407...], [8.92..., 44.407...]], "type": "LineString"}

#print(isolines[7][0].split(";")[1])

###jak zbudowac geojsona:
#n [15]: line = LineString([ (1,1), (2,2)])

#n [16]: line
#ut[16]: {"coordinates": [[1, 1], [2, 2]], "type": "LineString"}

#n [17]:

## jak dodac propertisy
#------ Feature(geometry=my_point, properties={"country": "Spain"})



#print("".join([el.replace('\n', ';') for el in file_lines  if re.match(r'^IsoValue.*$'  , el)]))

#filtered = filter(lambda x: not re.match(r'^\s*$', x), original)
