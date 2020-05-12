import json
import itertools

def flatten(lst): ## refactor - zrobic klase list flatting tools?
	for x in lst:
		if isinstance(x, list):
			for x in flatten(x):
				yield x
		else:
			yield x

def flat_into_tuples(nested_list):
	flatten_list = list(flatten(nested_list))
	return list(zip(flatten_list[0::2], flatten_list[1::2]))


class Converter:
	def __init__(self, field=';', line='\n', object='\n\n'):
		self.field = field
		self.line = line
		self.object = object

	def convert(self, data):
		result = self.build_header(data)
		for feature in self.get_features(data):
			result += self.build_feature(feature)
		return result

	def build_header(self, data, coord_X="X", coord_Y="Y"):
		return coord_X + self.field + coord_Y + self.field + \
		 	   self.field.join(data['features'][0]['properties'].keys()) + \
			   self.field + self.line

	def build_coordinates(self, coordinates):
		return self.field.join([str(el) for el in coordinates ]) + self.field

	def build_properties(self,_dict):
		return self.field.join(str(el[1]) for el in _dict.items()) + self.field

	def build_point(self,xy,properties):
		return self.build_coordinates(xy) + self.build_properties(properties) + self.line

	def build_feature(self, feature):
		result = ""
		properties = self.get_properties(feature)
		for xy in self.get_coordinates(feature):
			result += self.build_point(xy, properties)
		return result + self.object

	def get_properties(self, feature):
		return feature['properties']

	def get_features(self, data):
		return data['features']

	def get_coordinates(self,feature):
		return flat_into_tuples(feature['geometry']['coordinates'])
