#!/usr/bin/env python3

import sys
import os
import sqlite3
import requests
import json
import urllib
import pandas as pd


def get_aqi_data(city, token):
    aqi_data_url = 'http://api.waqi.info/feed/' + city + '/?token=' + token
    try:
        api_request = urllib.request.Request(aqi_data_url)
        api_response = urllib.request.urlopen(api_request)

        try:
            return json.loads(api_response.read())
        except (EOFError, KeyError, TypeError):
            return "JSON error"

    except IOError as e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason


city = 'astana'
token = '153147500b88026a9bc053bdf5c2b382cb90e806'
url = 'http://api.waqi.info/feed/' + city + '/?token=' + token
page_data = get_aqi_data(city, token)

print('URL:', page_data)

alert = ''
value = page_data['data']['iaqi']['pm25']['v']

# alert if hazardous
if 0 < value <= 50:
        print('Загрязнение воздуха - низкое')
elif 50 < value <= 100:
        print('Загрязнение воздуха - ниже среднего')
elif 100 < value <= 150:
        print('Загрязнение воздуха - среднее')
elif 150 < value <= 200:
        print('Загрязнение воздуха - выше среднего')
elif 200 < value <= 250:
        print('Загрязнение воздуха - высокое')
elif 250 < value <= 300:
        print('Загрязнение воздуха - опасное')
else:
        print('Нет данных')


# create DB
database = sqlite3.connect('Astana.db')
cur = database.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS AirData
              (Number INT, DateT Datetime, PM25 INT)''')

for i in range(1):
    Number = i
    DateT = page_data['data']['time']['s']
    PM25 = page_data['data']['iaqi']['pm25']['v']

    print('Number', Number, 'Date', DateT, 'PM25', PM25)
    for ins in [(Number, DateT, PM25),
                ]:
        cur.execute('INSERT INTO AirData(Number, DateT, PM25) VALUES (?,?,?)', ins)

database.commit()
cur.close()
database.close()

