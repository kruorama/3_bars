# Ближайшие бары

Скрипт читает файл bars.json, вычисляет самый большой и самый маленький бар по количеству мест, запрашивает координаты пользователя и вычисляет ближайший бар по прямой без учета кривизны Земли. Вычисляется квадрат дистанции, чтобы не импортировать модуль math


# Где взять файл

На сайте data.mos.ru есть много разных данных, в том числе список московских баров. Его можно скачать в формате JSON. Для этого нужно:

- зарегистрироваться на сайте и получить ключ API;
- скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.
А можно не тратить на это время и воспользоваться ранее скачанным файлом: https://devman.org/fshare/1503831681/4/

Схема файла не проверяется, только доступность ['features'] в bars_dict

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <filepath>
# possibly requires call of python3 executive instead of just python
Input latitude: 55.880913782721215
Input longitude: 37.449701840999658


Biggest bar
{
    "geometry": {
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ],
        "type": "Point"
    },
    "properties": {
        "DatasetId": 1796,
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
        "Attributes": {
            "global_id": 169375059,
            "Name": "Спорт бар «Красная машина»",
            "IsNetObject": "нет",
            "OperatingCompany": null,
            "AdmArea": "Южный административный округ",
            "District": "Даниловский район",
            "Address": "Автозаводская улица, дом 23, строение 1",
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "SeatsCount": 450,
            "SocialPrivileges": "нет"
        }
    },
    "type": "Feature"
}


Smallest bar
{
    "geometry": {
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ],
        "type": "Point"
    },
    "properties": {
        "DatasetId": 1796,
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53",
        "Attributes": {
            "global_id": 20675518,
            "Name": "БАР. СОКИ",
            "IsNetObject": "нет",
            "OperatingCompany": null,
            "AdmArea": "Северо-Западный административный округ",
            "District": "район Митино",
            "Address": "Дубравная улица, дом 34/29",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ],
            "SeatsCount": 0,
            "SocialPrivileges": "нет"
        }
    },
    "type": "Feature"
}


Smallest bar
{
    "geometry": {
        "coordinates": [
            37.44970184099966,
            55.880913782721215
        ],
        "type": "Point"
    },
    "properties": {
        "DatasetId": 1796,
        "VersionNumber": 2,
        "ReleaseNumber": 2,
        "RowId": "2f48cac2-ea87-4ace-9079-f46848485e78",
        "Attributes": {
            "global_id": 20661309,
            "Name": "Бар IMAX",
            "IsNetObject": "нет",
            "OperatingCompany": null,
            "AdmArea": "Северный административный округ",
            "District": "район Левобережный",
            "Address": "Правобережная улица, дом 1Б",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 775-77-79"
                }
            ],
            "SeatsCount": 4,
            "SocialPrivileges": "нет"
        }
    },
    "type": "Feature"
}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
