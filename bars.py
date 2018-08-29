import json
import math

def pretty_print(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)

data = load_data('bars.json')

array = data['features']



def get_biggest_bar(data):
    max_value = None #set to none so that there is no default value
    max_bar = None

    for bar in data:
        seats_count = int(bar['properties']['Attributes']['SeatsCount'])

        if max_value is None or seats_count > max_value: # is None instead of == None (second will return True if not empty)
            max_value = seats_count

        if seats_count >= max_value:
            max_bar = bar
    
    bar_info = 'Самый большой бар: ' + max_bar['properties']['Attributes']['Name'] + ', ' + str(max_bar['properties']['Attributes']['SeatsCount'])

    return bar_info

print (get_biggest_bar(array))


def get_smallest_bar(data):
    min_value = None #set to none so that there is no default value
    min_bar = None

    for bar in data:
        seats_count = int(bar['properties']['Attributes']['SeatsCount'])

        if min_value is None or seats_count < min_value: # is None instead of == None (second will return True if not empty)
            min_value = seats_count

        if seats_count <= min_value:
            min_bar = bar
    
    bar_info = 'Самый маленький бар: ' + min_bar['properties']['Attributes']['Name'] + ', ' + str(min_bar['properties']['Attributes']['SeatsCount'])

    return bar_info

print (get_smallest_bar(array))




def get_closest_bar(data):

    min_dist = None
    closest_bar = None

    # Point one
    lon1 = longitude = float(input("Please enter longitude: "))
    lat1 = float(input("Please enter longitude: "))
    

    for bar in data:
        # Point two
        lon2 = float(bar['geometry']['coordinates'][0])
        lat2 = float(bar['geometry']['coordinates'][1])

        dist = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

        if min_dist is None or dist < min_dist:
            min_dist = dist

        if dist <= min_dist:
            closest_bar = bar

        bar_info = 'Самый близкий бар: ' + closest_bar['properties']['Attributes']['Name']

    return bar_info



print(get_closest_bar(array))

