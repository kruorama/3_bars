import json
import sys


def read_bars_lst(filepath):
    with open(filepath, 'r') as file_handler:
        bars_json = json.load(file_handler)
        return bars_json


def get_bars_lst(bars_json):
    bars = bars_json['features']
    return bars


def get_biggest_bar(bars):
    max_bar = max(
        bars,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return max_bar


def get_smallest_bar(bars):
    min_bar = min(
        bars,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return min_bar


def get_closest_bar(bars):

    # I don't know how to use min here without appending distance to the JSON

    min_square_dist = None
    closest_bar = None

    lon_current = longitude = float(input('Input longitude: '))
    lat_current = float(input('Input latitude: '))

    for bar in bars:
        lon_bar = float(bar['geometry']['coordinates'][0])
        lat_bar = float(bar['geometry']['coordinates'][1])

        square_dist = (lat_bar - lat_current)**2 + (lon_bar - lon_current)**2

        if min_square_dist is None or square_dist < min_square_dist:
            min_square_dist = square_dist

        if square_dist <= min_square_dist:
            closest_bar = bar

    return closest_bar


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit('Please add a path to bars list')

    bars_json = read_bars_lst(sys.argv[1])
    bars = get_bars_lst(bars_json)

    print('Biggest bar')
    print(get_biggest_bar(bars))
    print('Smallest bar')
    print(get_smallest_bar(bars))
    print('closest_bar')
    print(get_closest_bar(bars))
