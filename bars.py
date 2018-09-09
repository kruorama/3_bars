import json
import sys


def load_bars(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            bars_dict = json.load(file_handler)
            return None, bars_dict
    except json.decoder.JSONDecodeError:
        return 'parse error', None
    except FileNotFoundError:
        return 'no such file', None


def get_bars_lst(bars_dict):
    bars_lst = bars_dict['features']
    return bars_lst


def get_biggest_bar(bars_lst):
    max_bar = max(
        bars_lst,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return max_bar


def get_smallest_bar(bars_lst):
    min_bar = min(
        bars_lst,
        key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return min_bar


def get_current_latitude():
    try:
        current_latitude = float(input('Input latitude: '))
        if -90 < current_latitude < 90:
            return None, current_latitude
        else:
            return 'latitude is not between -90 and 90', None
    except ValueError:
        return 'latitude should be a number', None


def get_current_longitude():
    try:
        current_longitude = float(input('Input longitude: '))
        if -180 < current_longitude < 180:
            return None, current_longitude
        else:
            return 'longitude is not between -180 and 180', None
    except ValueError:
        return 'longitude should be a number', None


def get_square_distance(current_longitude, current_latitude, bar):
    lon_bar = bar['geometry']['coordinates'][0]
    lat_bar = bar['geometry']['coordinates'][1]
    square_dist = ((lat_bar - current_latitude) ** 2
                   + (lon_bar - current_longitude) ** 2)
    return square_dist


def get_closest_bar(bars_lst, current_latitude, current_longitude):
    closest_bar = min(
        bars_lst,
        key=lambda x: get_square_distance(
            current_longitude,
            current_latitude,
            x))
    return closest_bar


def print_bar(label, bar):
    bar_name = bar['properties']['Attributes']['Name']
    bar_district = bar['properties']['Attributes']['District']
    bar_address = bar['properties']['Attributes']['Address']
    bar_seats_count = bar['properties']['Attributes']['SeatsCount']

    print('')
    print(label)
    print(bar_name)
    print('District: {}'.format(bar_district))
    print('Address: {}'.format(bar_address))
    print('Seats: {}'.format(bar_seats_count))


def print_all_bars(bars_lst, current_latitude, current_longitude):
    print_bar('Biggest bar', get_biggest_bar(bars_lst))
    print_bar('Smallest bar', get_smallest_bar(bars_lst))
    print_bar('Closest_bar',
              get_closest_bar(bars_lst, current_latitude, current_longitude))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit('Please add a path to bars list')

    error, bars_dict = load_bars(sys.argv[1])

    if bars_dict is None:
        exit('Error: {}'.format(error))
    else:
        try:
            bars_lst = get_bars_lst(bars_dict)
        except KeyError:
            exit('That doesn\'t seem like correct bars.json')

    error, current_latitude = get_current_latitude()
    if current_latitude is None:
        exit('Error: {}'.format(error))

    error, current_longitude = get_current_longitude()
    if current_longitude is None:
        exit('Error: {}'.format(error))

    print_all_bars(bars_lst, current_latitude, current_longitude)
