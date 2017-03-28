from __future__ import unicode_literals
from utils import lookup, getCategoryNumber, getStateNumber
from django.db import models
import re


# API call can be implemented by using URLlib2 (https://docs.python.org/2/library/urllib2.html)
# JSON can be implemented by using JSON library (https://docs.python.org/2/library/json.html)

class RemoteResponse:
    def __init__(self, type, categories, states, startingDate, endingDate):
        
        # translate the human readable thing to 0.1 0.2 thing (ABS query)
        # note we are using getStateNumber and getCategoryNumber directly.. not using utils.lookup
        stateNumbers = list(map(getStateNumber, states))
        categoryNumbers = list(map(getCategoryNumber, categories))
        
        # convert 'YYYY-MM-DD' to 'YYYY-MM'
        startMonth = re.sub(r'(\d{4}-\d{2})-\d{2}',r'\1', startingDate)
        endMonth = re.sub(r'(\d{4}-\d{2})-\d{2}',r'\1', endingDate)
        
        # query ABS and get the result
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        values = {'startTime':startMonth, 'endTime': endMonth, 'dimensionAtObservation': 'allDimensions'}
        data = urllib.urlencode(values)

        url = 'http://stat.data.abs.gov.au/sdmx-json/data/RT/'

        plus = "+"
        statesString = plus.join(stateNumbers)
        categoriesString = plus.join(categoryNumbers)

        # URL Format: url/{states-numbers}.{data-type}.{categories-numbers}.{adjustment-type(original/seasonal/trend)}.M(monthly data)/all
        url = url + statesString + ".2." + categoriesString + ".10.M/all"

        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        #print the_page


        # if normal
        # we set our own attribute to a normal state thing
        # else we set ourselves to a error state
        pass

    def toJSON(self):
        # should be a very easy function in JSON library I believe
        # pass in self
        pass

# sub class and super class python: http://stackoverflow.com/questions/1607612/python-how-do-i-make-a-subclass-from-a-superclass
class Merchandise(RemoteResponse):
    type = "merch"
    def __init__(self,categories, states, startingDate, endingDate):
        RemoteResponse.__init__(self, Merchandise.type ,categories, states, startingDate, endingDate)
        # super somthing

# same as above
class Retail(RemoteResponse):
    type = "Retail"
    def __init__(self, categories, states, startingDate, endingDate):
        RemoteResponse.__init__(self, Retail.type, categories, states, startingDate, endingDate)
        # super somthing
