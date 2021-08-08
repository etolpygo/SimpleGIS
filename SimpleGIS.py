import turtle as t
import json

states = dict()
  
# open state coordinates JSON file
f = open('gz_2010_us_040_00_500k.json')
  
# return JSON object as a dictionary
data = json.load(f)
  
# iterate through data and populate states dictionary
for i in data['features']:
    name = i['properties']['NAME']
    coordinates = i['geometry']['coordinates']
    states[name] = { 'coordinates': coordinates }
  
# Closing file
f.close()

# for testing
from pprint import pprint
pprint(states)