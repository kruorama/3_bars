import json
import argparse


def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Input file and current coordinates')

    parser.add_argument(
        'filepath',
        help='Path to JSON file with bars')

    parser.add_argument(
        'current_latitude',
        help='Your current latitude',
        type=float)

    parser.add_argument(
        'current_longitude',
        help='Your current latitude',
        type=float)

    args = parser.parse_args()
    return args


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


def get_square_distance(current_longitude, current_latitude, bar):
    lon_bar = bar['geometry']['coordinates'][0]
    lat_bar = bar['geometry']['coordinates'][1]
    square_dist = ((lat_bar - current_latitude) ** 2
                   + (lon_bar - current_longitude) ** 2)
    return square_dist


def get_closest_bar(bars_lst, current_latitude, current_longitude):
    if (current_latitude > 90) or (current_latitude < -90):
        raise ValueError('Latitude is not between -90 and 90.')

    if (current_longitude > 180) or (current_longitude < -180):
        raise ValueError('Longitude is not between -180 and 180')

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


if __name__ == '__main__':
    args = get_parser_args()

    error, bars_dict = load_bars(args.filepath)

    if bars_dict is None:
        exit('Error: {}'.format(error))

    try:
        bars_lst = get_bars_lst(bars_dict)
        print_bar('Biggest bar', get_biggest_bar(bars_lst))
        print_bar('Smallest bar', get_smallest_bar(bars_lst))
        print_bar('Closest_bar',
                  get_closest_bar(bars_lst,
                                  args.lat,
                                  args.lon))
    except KeyError:
        exit("That doesn't seem like correct bars.json")
    except ValueError as error:
        exit('Error: {}'.format(error))
