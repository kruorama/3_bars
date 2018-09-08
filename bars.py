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


def get_lat_current():
    while True:
        try:
            lat_current = float(input('Input latitude: '))
            if -90 < lat_current < 90:
                break
            else:
                print("Latitude should be between -90 and 90. Try again...")
        except ValueError:
            print("That was not a valid number.  Try again...")
    return lat_current


def get_lon_current():
    while True:
        try:
            lon_current = float(input('Input longitude: '))
            if -180 < lon_current < 180:
                break
            else:
                print("Longitude should be between -180 and 180. Try again...")
        except ValueError:
            print("That was not a valid number.  Try again...")

    return lon_current


def get_square_distance(lon_current, lat_current, bar):
    lon_bar = bar['geometry']['coordinates'][0]
    lat_bar = bar['geometry']['coordinates'][1]
    square_dist = (lat_bar - lat_current) ** 2 + (lon_bar - lon_current) ** 2
    return square_dist


def get_closest_bar(bars_lst):
    lat_current = get_lat_current()
    lon_current = get_lon_current()
    closest_bar = min(
        bars_lst,
        key=lambda x: get_square_distance(lon_current, lat_current, x))
    return closest_bar


def print_bar(label, bar):
    print('')
    print('')
    print(label)
    print(json.dumps(bar, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        exit('Please add a path to bars list')

    error, bars_dict = load_bars(sys.argv[1])

    if bars_dict is None:
        print('Error: ' + error)
        exit()
    else:
        try:
            bars_lst = get_bars_lst(bars_dict)
        except KeyError:
            print("That doesn't seem like correct bars.json")
            exit()

    print_bar("Biggest bar", get_biggest_bar(bars_lst))
    print_bar("Smallest bar", get_smallest_bar(bars_lst))
    print_bar("Closest bar", get_closest_bar(bars_lst))
