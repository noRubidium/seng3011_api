from __future__ import unicode_literals
from utils import lookup, getCategoryNumber, getStateNumber
from django.db import models
import re


# API call can be implemented by using URLlib2 (https://docs.python.org/2/library/urllib2.html)
# JSON can be implemented by using JSON library (https://docs.python.org/2/library/json.html)

class RemoteResponse:
    def __init__(self, type, categories, states, startingDate, endingDate):
        
        # translate the human readable thing to 0.1 0.2 thing (ABS query)
        # note we are using getStateNumber directly.. not using utils.lookup
        self.stateNumbers = map(getStateNumber, states)
        
        # convert 'YYYY-MM-DD' to 'YYYY-MM'
        self.startMonth = re.sub(r'(\d{4}-\d{2})-\d{2}',r'\1', startingDate)
        self.endMonth = re.sub(r'(\d{4}-\d{2})-\d{2}',r'\1', endingDate)

        # common variables used for abs api query 
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        values = {'startTime':startMonth, 'endTime': endMonth, 'dimensionAtObservation': 'allDimensions'}
        data = urllib.urlencode(values)
        url = 'http://stat.data.abs.gov.au/sdmx-json/data/'

        if (type == 'merch'):

            self.categoryNumbers = map(getCommodityNumber, categories)

            plus = "+"
            statesString = plus.join(self.stateNumbers)
            categoriesString = plus.join(self.categoryNumbers)

            # URL Format: url/MERCH_EXP/{states-numbers}.{categories-numbers}.{industry-of-origin}.{country-of-dest}.M(monthly data)/all
            url = url + 'MERCH_EXP/' + statesString + "." + categoriesString + ".-1.-.M/all"


        elif (type == 'retail'):

            self.categoryNumbers = map(getCategoryNumber, categories)

            plus = "+"
            statesString = plus.join(self.stateNumbers)
            categoriesString = plus.join(self.categoryNumbers)

            # URL Format: url/RT/{states-numbers}.{data-type}.{categories-numbers}.{adjustment-type(original/seasonal/trend)}.M(monthly data)/all
            url = url + 'RT/' + statesString + ".2." + categoriesString + ".10.M/all"

        
        # query ABS and get the result

        # if normal
        # we set our own attribute to a normal state thing
        try:
            req = urllib2.Request(url + "?" + data, None, headers)
            response = urllib2.urlopen(req)
            self.response_data = json.loads(response.read())
            self.response_status = "normal"

        # else we set ourselves to a error state
        except:
            self.response_status = "error"

    def getJSON(self):
        # should be a very easy function in JSON library I believe
        # pass in self
        return self.response_data

    def getStatus(self):
        return self.response_status

# sub class and super class python: http://stackoverflow.com/questions/1607612/python-how-do-i-make-a-subclass-from-a-superclass
class Merchandise(RemoteResponse):
    type = "merch"
    def __init__(self,categories, states, startingDate, endingDate):
        RemoteResponse.__init__(self, Merchandise.type ,categories, states, startingDate, endingDate)

# same as above
class Retail(RemoteResponse):
    type = "retail"
    def __init__(self, categories, states, startingDate, endingDate):
        RemoteResponse.__init__(self, Retail.type, categories, states, startingDate, endingDate)
        # super somthing
