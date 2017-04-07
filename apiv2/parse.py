#!/usr/bin/python
"""
Parse all the json
"""
import json
from .utils import get_date_end, get_state_name, reverse_map_categories, reverse_map_commodities


def to_int_list(observation):
    """
    Change observation to int list
    :param observation: "0:0"
    :return: list of int
    """
    return map(int, observation.encode().split(':'))


def parse_merchandise(data):
    """
    parse the merchandise json response data
    :param data: json data
    :return: json object of cleaned up data
    """

    states = {}
    commodities = {}
    months = {}

    merch_switch = {
        'REGION': (states, 'id'),
        'SITC_REV3': (commodities, 'id'),
        'TIME_PERIOD': (months, 'name')
    }

    lookup = data['structure']['dimensions']['observation']
    for i in lookup:
        (current, key_name) = merch_switch.get(i['id'], (None, None))
        if current is not None:
            index = 0
            for curr_item in i['values']:
                current[index] = curr_item[key_name]
                index += 1

    result = {'MonthlyCommodityExportData': [{} for _ in xrange(len(commodities))]}

    for dataset in data['dataSets']:
        for observation, item in dataset['observations'].items():
            (state, commodity, _, _, _, month) = to_int_list(observation)

            curr = result['MonthlyCommodityExportData'][commodity]
            if 'commodity' not in curr:
                curr['commodity'] = reverse_map_commodities(commodities[commodity])
            if 'regional_data' not in curr:
                curr['regional_data'] = [{} for _ in xrange(len(states))]

            regional_data = curr['regional_data'][state]
            if 'state' not in regional_data:
                regional_data['state'] = get_state_name(states[state])
            if 'data' not in regional_data:
                regional_data['data'] = [{} for _ in xrange(len(months))]

            regional_data['data'][month]['date'] = get_date_end(months[month])
            regional_data['data'][month]['value'] = item[0]

    return result


def parse_retail(data):
    """
    parse the retail json response data
    :param data: json data
    :return: json object of cleaned up data
    """

    states = {}
    categories = {}
    months = {}

    retail_switch = {
        'ASGC_2010': (states, 'id'),
        'IND_R': (categories, 'id'),
        'TIME_PERIOD': (months, 'name')
    }

    lookup = data['structure']['dimensions']['observation']
    for i in lookup:
        (curr, key_name) = retail_switch.get(i['id'], (None, None))
        if curr is not None:
            index = 0
            for item in i['values']:
                curr[index] = item[key_name]
                index += 1

    result = {'MonthlyRetailData': [{} for _ in xrange(len(categories))]}

    for dataset in data['dataSets']:
        for observation, item in dataset['observations'].items():
            (state, _, category, _, _, month) = to_int_list(observation)

            curr = result['MonthlyRetailData'][category]
            if 'category' not in curr:
                curr['category'] = reverse_map_categories(categories[category])
            if 'regional_data' not in curr:
                curr['regional_data'] = [{} for _ in xrange(len(states))]

            regional_data = curr['regional_data'][state]
            if 'state' not in regional_data:
                regional_data['state'] = get_state_name(states[state])
            if 'data' not in regional_data:
                regional_data['data'] = [{} for _ in xrange(len(months))]

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
