from __future__ import unicode_literals
from utils import lookup
from django.db import models



# API call can be implemented by using URLlib2 (https://docs.python.org/2/library/urllib2.html)
# JSON can be implemented by using JSON library (https://docs.python.org/2/library/json.html)

class RemoteResponse:
    def __init__(self, type, categories, states, startingDate, endingDate):
        # translate the human readable thing to 0.1 0.2 thing (ABS query)
        map(lookup, categories)
        # query ABS and get the result
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
    def __init__(self, categories, states, startingDate, endingDate):
        self.type = "merch"
        # super somthing

# same as above
class Retail(RemoteResponse):
    def __init__(self, categories, states, startingDate, endingDate):
        self.type = "retail"
        # super somthing