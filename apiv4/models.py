"""
Model handles all the API calls stuff
"""
from __future__ import unicode_literals
# from django.db import models
import json
import re
import urllib
import urllib2
import logging
import time

from .parse import parse_merchandise, parse_retail
from .utils import get_state_number_retail, get_state_number_merch, \
    get_category_number, get_commodity_number, validate_date, \
    LookupNotFoundError, InvalidDateError, AVAILABLE_STATES, \
    AVAILABLE_COMMODITIES, AVAILABLE_CATEGORIES

current_date = time.strftime("%Y-%m-%d")


# configure logging formatting
logging.basicConfig(filename="{}.log".format(current_date), level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def date_to_month(date):
    """
    Change from date to month
    :param date: String 'YYYY-MM-DD'
    :return: 'YYYY-MM'
    """
    return re.sub(r'(\d{4}-\d{2})-\d{2}', r'\1', date)


def disassemble_json(arr, k1, k2):
    """
    Disassemble the json into dictionary
    :param arr: the array of categories
    :param k1: category or commodities
    :param k2: value or turnovers
    :return: 
    """
    result = {}
    for cat in arr:
        name = cat[k1]
        regional_data = cat['regional_data']
        result[name] = {}
        for d in regional_data:
            print d
            try:
                state = d['state']
                result[name][state] = {}
                for data in d['data']:
                    try:
                        result[name][state][data['date']] = data[k2]
                    except KeyError:
                        pass
            except KeyError:
                pass
    return result


class RemoteResponse(object):
    """
    API model type, query from remote ABS API
    """
    type = None
    last_update_month = None
    global_status = {'status': 'normal'}
    total_dict = None

    def __init__(self, categories, states, starting_date, ending_date):
        (starting_date, ending_date) = validate_date(starting_date, ending_date)

        current_month = time.strftime("%Y-%m")

        if current_month != RemoteResponse.last_update_month or RemoteResponse.global_status['status'] != 'normal':
            RemoteResponse.update()
        self.response_status, self.response_data = self.cache_get(categories, states, starting_date, ending_date)

    @staticmethod
    def update():
        RemoteResponse.total_dict = dict()
        RemoteResponse.remote_get('merch', AVAILABLE_COMMODITIES, AVAILABLE_STATES, '1970-01-01', current_date)
        RemoteResponse.remote_get('retail', AVAILABLE_CATEGORIES, AVAILABLE_STATES, '1970-01-01', current_date)

    @staticmethod
    def remote_get(remote_type, categories, states, starting_date, ending_date):

        # common variables used for abs api query
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        values = {'startTime': date_to_month(starting_date),
                  'endTime': date_to_month(ending_date),
                  'dimensionAtObservation': 'allDimensions'}
        data = urllib.urlencode(values)
        url = 'http://stat.data.abs.gov.au/sdmx-json/data/'
        plus = '+'

        if remote_type == 'merch':
            categories_string = plus.join(map(get_commodity_number, categories))

            # translate the human readable thing to 0.1 0.2 thing (ABS query)
            # note we are using get_state_number directly.. not using utils.lookup
            states_string = plus.join(map(get_state_number_merch, states))

            # URL Format: url/MERCH_EXP/{states-numbers}.{categories-numbers}
            # .{industry-of-origin}.{country-of-dest}.M(monthly data)/all
            url += 'MERCH_EXP/' + states_string + "." + categories_string + ".-1.-.M/all"

        elif remote_type == 'retail':
            categories_string = plus.join(map(get_category_number, categories))

            # translate the human readable thing to 0.1 0.2 thing (ABS query)
            # note we are using get_state_number directly.. not using utils.lookup
            states_string = plus.join(map(get_state_number_retail, states))
            # URL Format: url/RT/{states-numbers}.{data-type}.{categories-numbers}
            # .{adjustment-type(original/seasonal/trend)}.M(monthly data)/all
            url += 'RT/' + states_string + ".2." + categories_string + ".10.M/all"

        # query ABS and get the result
        # if normal
        # we set our own attribute to a normal state thing
        try:
            print url + "?" + data

            # start timer and add log entry for ABS call
            start_time = time.time()
            logger.info("Making ABS call: {}?{}".format(url, data))

            req = urllib2.Request(url + '?' + data, None, headers)
            response = urllib2.urlopen(req)

            # end timer, update status and data variables, and add log entry for successful call
            end_time = time.time()
            ms_elapsed = (end_time - start_time)*1000

            if remote_type == 'merch':
                RemoteResponse.total_dict['merch'] = disassemble_json(parse_merchandise(json.loads(response.read()))['MonthlyCommodityExportData'], 'commodity',
                                                                  'value')
            else:
                RemoteResponse.total_dict['retail'] = disassemble_json(parse_retail(json.loads(response.read()))['MonthlyRetailData'], 'category',
                                                                   'turnover')
            logger.info("ABS Response OK: '{}?{}'. Time taken: {}ms".format(url, data, ms_elapsed))
            RemoteResponse.last_update_month = time.strftime("%Y-%m")
        except urllib2.HTTPError as error:
            RemoteResponse.global_status = {'status': 'error', 'error': "Results not found. ABS does not have the data for the requested dates."}
            # add log entry for error
            logger.info("ABS Response ERROR: '{}?{}': ".format(url, data, error))

    def get_json(self):
        """
        :return: Return json of response
        """
        return self.response_data

    def get_status(self):
        """
        :return: check if the api call exit normally
        """
        return self.response_status

    def cache_get(self, categories, states, starting_date, ending_date):
        result = {}
        top_level_key = 'MonthlyCommodityExportData' if self.type == 'merch' else 'MonthlyRetailData'
        k1 = 'commodity' if self.type == 'merch' else 'category'
        k2 = 'value' if self.type == 'merch' else 'turnover'
        total_list = []
        try:
            for cat in categories:
                # force error
                if self.type == 'merch':
                    get_commodity_number(cat)
                else:
                    get_category_number(cat)

                regional_data = []
                for state in states:
                    # force lookup error
                    if self.type == 'merch':
                        get_state_number_merch(state)
                    else:
                        get_state_number_retail(state)

                    values = []
                    for date in RemoteResponse.total_dict[self.type][cat][state]:

                        if starting_date <= date <= ending_date:
                            values.append({'date': date, k2: RemoteResponse.total_dict[self.type][cat][state][date]})
                    regional_data.append({'state': state, 'data': values})
                total_list.append({k1: cat, 'regional_data': regional_data})
        except LookupNotFoundError as error:
            # add log entry for error
            logger.info("Local lookup error: '{}': ".format(error))
            return 'error', {'error': str(error)}

        result[top_level_key] = total_list
        return 'normal', result


# sub class and super class python:
# http://stackoverflow.com/questions/1607612/python-how-do-i-make-a-subclass-from-a-superclass
class Merchandise(RemoteResponse):
    """
    Merchandise Data Type
    """
    type = 'merch'

    def __init__(self, categories, states, starting_date, ending_date):
        RemoteResponse.__init__(self, categories, states, starting_date, ending_date)


# same as above
class Retail(RemoteResponse):
    """
    Retail data type
    """
    type = 'retail'

    def __init__(self, categories, states, starting_date, ending_date):
        RemoteResponse.__init__(self, categories, states, starting_date, ending_date)
