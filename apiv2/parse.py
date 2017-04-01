#!/usr/bin/python
"""
Parse all the json
"""
import json
from .utils import get_date_end, get_state_name, reverse_map_categories, reverse_map_commodities


def parse_merchandise(data):
    """
    parse the merchandise json response data
    :param data: json data
    :return: json object of cleaned up data
    """
    lookup = data['structure']['dimensions']['observation']

    states = {}
    commodities = {}
    months = {}
    merch_switch = {
        'REGION': (states, 'id'),
        'SITC_REV3': (commodities, 'id'),
        'TIME_PERIOD': (months, 'name')
    }
    for i in lookup:
        key_id = i['id']
        (curr, key_name) = merch_switch.get(key_id, (None, None))
        if curr is not None:
            index = 0
            for item in i['values']:
                curr[index] = item[key_name]
                index += 1

    result = {'MonthlyCommodityExportData': [{} for _ in range(0, len(commodities))]}
    export_data = result['MonthlyCommodityExportData']

    for dataset in data['dataSets']:
        for observation, item in dataset['observations'].items():
            (state, commodity, _, _, _, month) = [int(i) for i in observation.encode().split(':')]

            table = export_data[commodity]
            if 'commodity' not in table:
                table['commodity'] = reverse_map_commodities(commodities[commodity])
            if 'regional_data' not in table:
                table['regional_data'] = [{} for _ in range(0, len(states))]

            regional_data = table['regional_data'][state]
            if 'state' not in regional_data:
                regional_data['state'] = get_state_name(str(states[state]))
            if 'data' not in regional_data:
                regional_data['data'] = [{} for _ in range(0, len(months))]

            regional_data['data'][month]['date'] = get_date_end(months[month])
            regional_data['data'][month]['value'] = item[0]

    return result


def parse_retail(data):
    """
    parse the retail json response data
    :param data: json data
    :return: json object of cleaned up data
    """
    lookup = data['structure']['dimensions']['observation']

    states = {}
    categories = {}
    months = {}
    retail_switch = {
        'ASGC_2010': (states, 'id'),
        'IND_R': (categories, 'id'),
        'TIME_PERIOD': (months, 'name')
    }

    for i in lookup:
        key_id = i['id']
        (curr, key_name) = retail_switch.get(key_id, (None, None))
        if curr is not None:
            index = 0
            for item in i['values']:
                curr[index] = item[key_name]
                index += 1
                # if key_id == 'IND_R':
                #     index = 0
                #     for category in i['values']:
                #         categories[index] = category['id']
                #         index += 1
                # if key_id == 'TIME_PERIOD':
                #     index = 0
                #     for month in i['values']:
                #         months[index] = month['name']
                #         index += 1

    result = {'MonthlyRetailData': [{} for _ in range(0, len(categories))]}
    retail_data = result['MonthlyRetailData']

    for dataset in data['dataSets']:
        for observation, item in dataset['observations'].items():
            (state, _, category, _, _, month) = [int(i) for i in observation.encode().split(':')]

            table = retail_data[category]
            if 'category' not in table:
                table['category'] = reverse_map_categories(categories[category])
            if 'regional_data' not in table:
                table['regional_data'] = [{} for _ in xrange(0, len(states))]

            regional_data = table['regional_data'][state]
            if 'state' not in regional_data:
                regional_data['state'] = get_state_name(str(states[state]))
            if 'data' not in regional_data:
                regional_data['data'] = [{} for _ in xrange(0, len(months))]

            regional_data['data'][month]['date'] = get_date_end(months[month])
            regional_data['data'][month]['turnover'] = item[0]

    return result


if __name__ == '__main__':
    TEST_DATA_FILE = open("./test_data/merch_test", 'r')
    print json.dumps(parse_merchandise(json.loads(TEST_DATA_FILE.read())))
    TEST_DATA_FILE.close()
    TEST_DATA_FILE = open("./test_data/retail_test", 'r')
    print json.dumps(parse_retail(json.loads(TEST_DATA_FILE.read())))
    TEST_DATA_FILE.close()
