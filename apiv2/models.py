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

from .utils import get_state_number_retail, get_state_number_merch, \
    get_category_number, get_commodity_number, validate_date, \
    LookupNotFoundError, InvalidDateError

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


class RemoteResponse(object):
    """
    API model type, query from remote ABS API
    """
    type = None

    def __init__(self, categories, states, starting_date, ending_date):
        validate_date(starting_date, ending_date)

        # common variables used for abs api query
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        values = {'startTime': date_to_month(starting_date),
                  'endTime': date_to_month(ending_date),
                  'dimensionAtObservation': 'allDimensions'}
        data = urllib.urlencode(values)
        url = 'http://stat.data.abs.gov.au/sdmx-json/data/'
        plus = '+'

        if self.type == 'merch':
            categories_string = plus.join(map(get_commodity_number, categories))

            # translate the human readable thing to 0.1 0.2 thing (ABS query)
            # note we are using get_state_number directly.. not using utils.lookup
            states_string = plus.join(map(get_state_number_merch, states))

            # URL Format: url/MERCH_EXP/{states-numbers}.{categories-numbers}
            # .{industry-of-origin}.{country-of-dest}.M(monthly data)/all
            url += 'MERCH_EXP/' + states_string + "." + categories_string + ".-1.-.M/all"

        elif self.type == 'retail':
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
            self.response_data = json.loads(response.read())
            self.response_status = 'normal'
            logger.info("ABS Response OK: '{}?{}'. Time taken: {}ms".format(url, data, ms_elapsed))

        # else we set ourselves to a error state
        except LookupNotFoundError as error:
            self.response_status = 'error'
            self.response_data = {'error': str(error)}
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
        