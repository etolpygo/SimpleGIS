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
# from pprint import pprint
# pprint(states)

map_width = 400
map_height = 300

# state = 'Colorado'
# points = states[state]['coordinates'][0]

state = 'California'
points = states[state]['coordinates'][10][0]

minx = 180
maxx = -180
miny = 90
maxy = -90

for x, y in points:
    if x < minx:
        minx = x
    elif x > maxx:
        maxx = x
    if y < miny:
        miny = y
    elif y > maxy:
        maxy = y
        
print(minx, maxx, miny, maxy)

dist_x = maxx - minx
dist_y = maxy - miny
x_ratio = map_width / dist_x
y_ratio = map_height / dist_y

def convert(point):
    lon = point[0]
    lat = point[1]
    x = map_width - ((maxx - lon) * x_ratio)
    y = map_height - ((maxy - lat) * y_ratio)
    # Python turtle graphics start in the
    # middle of the screen
    # so we must offset the points so they are centered
    x = x - (map_width/2)
    y = y - (map_height/2)
    return [x,y]
    

t.up()
first_pixel = None
for point in points:
    print(point)
    pixel = convert(point)
    if not first_pixel:
        first_pixel = pixel
    t.goto(pixel)
    t.down()
t.goto(first_pixel)
t.up()
t.goto([0,0])
t.write(state, align="center", font=("Arial",16,"bold"))
    
    
t.done()

