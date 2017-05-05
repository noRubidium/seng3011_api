"""
Model handles all the API calls stuff
"""
from .utils import data


class RetailData():
    def __init__(self, company_name):
        self.company_name = company_name
        self.get_data()

    def get_data(self):
        details = data[self.company_name]
        id = details.id
