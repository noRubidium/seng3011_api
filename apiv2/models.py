from __future__ import unicode_literals
from utils import lookup, get_state_number, get_category_number, get_commodity_number
from django.db import models
import re, urllib, urllib2, json


# API call can be implemented by using URLlib2 (https://docs.python.org/2/library/urllib2.html)
# JSON can be implemented by using JSON library (https://docs.python.org/2/library/json.html)
class RemoteResponse:
    def __init__(self, type, categories, states, starting_date, ending_date):
        
        # translate the human readable thing to 0.1 0.2 thing (ABS query)
        # note we are using get_state_number directly.. not using utils.lookup
        state_numbers = map(get_state_number, states)
        
        # convert 'YYYY-MM-DD' to 'YYYY-MM'
        start_month = re.sub(r'(\d{4}-\d{2})-\d{2}',r'\1', starting_date)
        end_month = re.sub(r'(\d{4}-\d{2})-\d{2}',r'\1', ending_date)

        # common variables used for abs api query 
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        values = {'startTime': start_month, 'endTime': end_month, 'dimensionAtObservation': 'allDimensions'}
        data = urllib.urlencode(values)
        url = 'http://stat.data.abs.gov.au/sdmx-json/data/'

        if type == 'merch':
            category_numbers = map(get_commodity_number, categories)
            plus = "+"
            states_string = plus.join(state_numbers)
            categories_string = plus.join(category_numbers)

            # URL Format: url/MERCH_EXP/{states-numbers}.{categories-numbers}.{industry-of-origin}.{country-of-dest}.M(monthly data)/all
            url += 'MERCH_EXP/' + states_string + "." + categories_string + ".-1.-.M/all"

        elif type == 'retail':
            category_numbers = map(get_category_number, categories)

            plus = "+"
            states_string = plus.join(state_numbers)
            categories_string = plus.join(category_numbers)

            # URL Format: url/RT/{states-numbers}.{data-type}.{categories-numbers}.{adjustment-type(original/seasonal/trend)}.M(monthly data)/all
            url += 'RT/' + states_string + ".2." + categories_string + ".10.M/all"

        # query ABS and get the result

        # if normal
        # we set our own attribute to a normal state thing
        try:
            req = urllib2.Request(url + "?" + data, None, headers)
            response = urllib2.urlopen(req)
            self.response_data = json.loads(response.read())
            self.response_status = "normal"

        # else we set ourselves to a error state
        except Exception as e:
            self.response_status = "error"
            self.response_data = {"erro_info": str(e)}

    def get_JSON(self):
        # should be a very easy function in JSON library I believe
        # pass in self
        return self.response_data

    def get_status(self):
        return self.response_status


# sub class and super class python:
# http://stackoverflow.com/questions/1607612/python-how-do-i-make-a-subclass-from-a-superclass
class Merchandise(RemoteResponse):
    type = 'merch'
    def __init__(self,categories, states, starting_date, ending_date):
        RemoteResponse.__init__(self, Merchandise.type ,categories, states, starting_date, ending_date)


# same as above
class Retail(RemoteResponse):
    type = 'retail'
    def __init__(self, categories, states, starting_date, ending_date):
        RemoteResponse.__init__(self, Retail.type, categories, states, starting_date, ending_date)
        # super somthing
