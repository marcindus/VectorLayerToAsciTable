from geojson import Point, Feature, FeatureCollection, dump

point = Point((-115.81, 37.24))

features = []
features.append(Feature(geometry=point, properties={"country": "Spain"}))

point2 = Point((-105.81, 39.24))
features.append(Feature(geometry=point2, properties={"country": "Spain"}))


feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as f:
   dump(feature_collection, f)
