import os
import json
import requests

from datetime import datetime, timedelta

import pandas as pd

ID_SITE = 109


def fetch_day(day_string):
    data = []
    filter_limit = 1000
    filter_offset = 0

    n_result = -1
    while n_result:
        url = 'http://stats.data.gouv.fr/?module=API&method=Live.getLastVisitsDetails&idSite={}&period=day&date={}&format=JSON&filter_offset={}&filter_limit={}'.format(ID_SITE, day_string, filter_offset, filter_limit)
        r = requests.get(url)

        assert r.status_code == 200
        assert r.encoding == 'utf-8'

        n_result
        data_batch = r.json()
        data += data_batch

        filter_offset += filter_limit
        n_result = len(data_batch)

    return data


def write_day(day_string):
    data = fetch_day(day_string)
    filename = 'logs/{}.json'.format(day_string)
    with open(filename, 'w') as f:
        json.dump(data, f)

def read_day(day_string):
    filename = '{}.json'.format(day_string)
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_last_n_month(n):
    a_month_ago = pd.datetime.today() + pd.DateOffset(months=-n)
    yesterday = pd.datetime.today() - pd.DateOffset(days=1)
    date_range = pd.date_range(a_month_ago, yesterday).strftime('%Y-%m-%d')
    for day in date_range:
        if day +'.json' not in os.listdir('logs/'):
            write_day(day)
            print('%s : done' % day)

write_last_n_month(1)
