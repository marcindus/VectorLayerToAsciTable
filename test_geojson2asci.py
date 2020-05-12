import unittest
import json
import sys, os
sys.path.append('C:\\Users\\duszek\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\sound_plan_export')

import geojson2asci


class Json2AsciConvertTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.buildings_osm = self.get_json_from_file("budynki.geojson")
        self.buildings_result = self.get_lines_from_asci_files("budynki.txt")

        self.roads_osm = self.get_json_from_file("drogi.geojson")
        self.roads_result = self.get_lines_from_asci_files("drogi.txt")
        self.converter = geojson2asci.Converter()

    def get_json_from_file(self, file_path):
        with open(file_path) as f:
            return json.load(f)

    def get_lines_from_asci_files(self, file_path):
        with open(file_path) as f:
            return f.readlines()

    def test_nested_list_flatten(self):
        nested_list = [[[[1,2],[1,2]]]]
        flat_list = [1,2,1,2]
        self.assertEqual(list(geojson2asci.flatten(nested_list)), flat_list)

    def test_nested_list_flatten_and_zipped_into_tuples(self):
        nested_list = [[[[1,2],[1,2]]]]
        my_zipped_flat_list = [(1,2),(1,2)]
        mylist = list(geojson2asci.flatten(nested_list))
        zipped = list(zip(mylist[0::2], mylist[1::2]))
        self.assertEqual(zipped, my_zipped_flat_list)


    def test_compare_first_line_converted_from_multipolygon_real_data_but_no_trailing_whitespaces(self):
        self.assertEqual(self.converter.convert(self.buildings_osm).split()[0].strip(), self.buildings_result[0].strip())

    def test_compare_first_line_converted_from_multipolygon_real_data_but_no_trailing_whitespaces2(self):
        self.assertEqual(self.converter.convert(self.buildings_osm).split()[2].strip(), self.buildings_result[2].strip())

    def test_compare_first_line_converted_from_linestring_real_data_but_no_trailing_whitespaces(self):
        self.assertEqual(self.converter.convert(self.roads_osm).split()[0].strip(), self.roads_result[0].strip())
