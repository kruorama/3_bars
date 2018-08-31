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
    max_bar_info = ('Самый большой бар: ' +
                    max_bar['properties']['Attributes']['Name'] +
                    ', ' +
                    str(max_bar['properties']['Attributes']['SeatsCount']) +
                    ', ' +
                    max_bar['properties']['Attributes']['Address'])
    return max_bar_info


print(get_biggest_bar(bars_lst))


def get_smallest_bar(bars):
    seats_counts = []
    min_bar = 0

    for bar in bars:
        seats_count = bar['properties']['Attributes']['SeatsCount']
        if seats_count > 0:  # a 0 seats bar makes no sense
            seats_counts.append(seats_count)
    min_seats = min(seats_counts)
    for bar in bars:
        if bar['properties']['Attributes']['SeatsCount'] == min_seats:
            min_bar = bar
    min_bar_info = ('Самый маленький бар: ' +
                    min_bar['properties']['Attributes']['Name'] +
                    ', ' +
                    str(min_bar['properties']['Attributes']['SeatsCount']) +
                    ', ' +
                    min_bar['properties']['Attributes']['Address'])
    return min_bar_info


print(get_smallest_bar(bars_lst))


def get_closest_bar(bars):

    min_dist = None
    closest_bar = None

    # Point one
    lon1 = longitude = float(input('Введите широту: '))
    lat1 = float(input('Введите долготу: '))

    for bar in bars:
        # Point two
        lon2 = float(bar['geometry']['coordinates'][0])
        lat2 = float(bar['geometry']['coordinates'][1])
        # comparing hypotenuse**2 since it doesn't change relative dist
        dist = (lat2 - lat1)**2 + (lon2 - lon1)**2

        if min_dist is None or dist < min_dist:
            min_dist = dist

        if dist <= min_dist:
            closest_bar = bar

        bar_info = ('Самый близкий бар: ' +
                    closest_bar['properties']['Attributes']['Name'] +
                    ', ' +
                    closest_bar['properties']['Attributes']['Address'])

    return bar_info


print(get_closest_bar(bars_lst))
