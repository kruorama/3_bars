import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


json_encoded = load_data('bars.json')
bars_lst = json_encoded['features']


def get_biggest_bar(bars):
    seats_counts = []
    max_bar = 0

    for bar in bars:
        seats_counts.append(bar['properties']['Attributes']['SeatsCount'])
    max_seats = max(seats_counts)
    for bar in bars:
        if bar['properties']['Attributes']['SeatsCount'] == max_seats:
            max_bar = bar
    return max_bar





def get_smallest_bar(bars):
    seats_counts = []
    min_bar = 0

    for bar in bars:
        seats_count = bar['properties']['Attributes']['SeatsCount']
        if seats_count > 0:
            seats_counts.append(seats_count)
    min_seats = min(seats_counts)
    for bar in bars:
        if bar['properties']['Attributes']['SeatsCount'] == min_seats:
            min_bar = bar
    return min_bar


def get_closest_bar(bars):

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
    print ('Biggest bar')
    print(get_biggest_bar(bars_lst))
    print('Smallest bar')
    print(get_smallest_bar(bars_lst))
    print('closest_bar')
    print(get_closest_bar(bars_lst))
