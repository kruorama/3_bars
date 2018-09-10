# Bars

The script reads the json file with bars and calculates biggest, smallest and closest bar

### Description

* Script takes a path to a file, latitude and longitude as parameters
* Shows errors if:
  * File is not found
  * File can't be read as JSON
  * Latitude is not between -90 and 90
  * Longitude is not between -180 and 180
* Doesn't check JSON's schema, will only work with a right JSON
* Calculates and prints the smallest and the biggest bars in file by seats count
* Calculates the closest bar to given coordinates (straight line, compares square distance to avoid importing `math`)


### Where to get bars.json

To download a list of all bars in Moscow from data.mos.ru in JSON format:
* Register on data.mos.ru and get an API key
* Download the file from a link like this https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.

Otherwise you can use a previously downloaded file: https://devman.org/fshare/1503831681/4/


### How to launch

Example of script launch on Linux, Python 3.5:

```bash

$ python bars.py <filepath> <current_latitude> <current_longitude>
# possibly requires call of python3 executive instead of just python

Biggest bar
Спорт бар «Красная машина»
District: Даниловский район
Address: Автозаводская улица, дом 23, строение 1
Seats: 450

Smallest bar
БАР. СОКИ
District: район Митино
Address: Дубравная улица, дом 34/29
Seats: 0

Closest_bar
Staropramen
District: Красносельский район
Address: Садовая-Спасская улица, дом 19, корпус 1
Seats: 50

```

### Project goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
