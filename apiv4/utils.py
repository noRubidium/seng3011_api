"""
    A lookup table thingy here ( states/category -> number)
"""
import re
import datetime
from dateutil.relativedelta import relativedelta


class LookupNotFoundError(Exception):
    """
    The error when lookup failed
    """

    def __init__(self, value):
        Exception.__init__(self, value)
        self.value = value

    def to_json(self):
        return {'error': self.value}


class InvalidDateError(Exception):
    """
    The error when lookup failed
    """

    def __init__(self, value):
        Exception.__init__(self, value)
        self.value = value

    def to_json(self):
        return {'error': self.value}


CATEGORIES = {
    'Total': '20',
    'Food': '41',
    'HouseholdGood': '42',
    'ClothingFootwareAndPersonalAccessory': '43',
    'DepartmentStores': '44',
    'CafesRestaurantsAndTakeawayFood': '46',
    'other': '45'
}

AVAILABLE_CATEGORIES = CATEGORIES.keys()

STATES = {
    'Total': '-',
    'AUS': '0',
    'NSW': '1',
    'WA': '5',
    'SA': '4',
    'ACT': '8',
    'VIC': '2',
    'TAS': '6',
    'QLD': '3',
    'NT': '7'
}

AVAILABLE_STATES = STATES.keys()

REVERSE_STATES = {
    '-': 'Total',
    '0': 'AUS',
    '1': 'NSW',
    '5': 'WA',
    '4': 'SA',
    '8': 'ACT',
    '2': 'VIC',
    '6': 'TAS',
    '3': 'QLD',
    '7': 'NT'
}

AVAILABLE_STATE_IDS = REVERSE_STATES.keys()

COMMODITIES = {
    'Total': '-1',
    'FoodAndLiveAnimals': '0',
    'BeveragesAndTobacco': '1',
    'CrudeMaterialAndInedible': '2',
    'MineralFuelLubricantAndRelatedMaterial': '3',
    'AnimalAndVegetableOilFatAndWaxes': '4',
    'ChemicalsAndRelatedProducts': '5',
    'ManufacturedGoods': '6',
    'MachineryAndTransportEquipments': '7',
    'OtherManufacturedArticles': '8',
    'Unclassified': '9'
}

AVAILABLE_COMMODITIES = COMMODITIES.keys()

REVERSE_CATEGORIES = {
    '20': 'Total',
    '41': 'Food',
    '42': 'HouseholdGood',
    '43': 'ClothingFootwareAndPersonalAccessory',
    '44': 'DepartmentStores',
    '46': 'CafesRestaurantsAndTakeawayFood',
    '45': 'other'
}

AVAILABLE_CATEGORY_IDS = REVERSE_CATEGORIES.keys()

REVERSE_COMMODITIES = {
    '-1': 'Total',
    '0': 'FoodAndLiveAnimals',
    '1': 'BeveragesAndTobacco',
    '2': 'CrudeMaterialAndInedible',
    '3': 'MineralFuelLubricantAndRelatedMaterial',
    '4': 'AnimalAndVegetableOilFatAndWaxes',
    '5': 'ChemicalsAndRelatedProducts',
    '6': 'ManufacturedGoods',
    '7': 'MachineryAndTransportEquipments',
    '8': 'OtherManufacturedArticles',
    '9': 'Unclassified'
}

AVAILABLE_COMMODITY_IDS = REVERSE_COMMODITIES.keys()
END_DATES_NUM = {
    '01': '{year}-01-31',
    '03': '{year}-03-31',
    '04': '{year}-04-30',
    '05': '{year}-05-31',
    '06': '{year}-06-30',
    '07': '{year}-07-31',
    '08': '{year}-08-31',
    '09': '{year}-09-30',
    '10': '{year}-10-31',
    '11': '{year}-11-30',
    '12': '{year}-12-31'
}
END_DATES = {
    'Jan': '{year}-01-31',
    'Mar': '{year}-03-31',
    'Apr': '{year}-04-30',
    'May': '{year}-05-31',
    'Jun': '{year}-06-30',
    'Jul': '{year}-07-31',
    'Aug': '{year}-08-31',
    'Sep': '{year}-09-30',
    'Oct': '{year}-10-31',
    'Nov': '{year}-11-30',
    'Dec': '{year}-12-31'
}

AVAILABLE_MONTHS = END_DATES.keys()

ERROR_FMT = 'The type you are requiring ({0}) doesn\'t exist. You should choose from {1}'
DATE_FORMAT_ERROR = '{0} date is invalid. Dates should be YYYY-MM-DD'
DATE_ERROR = '{0} date is invalid. There is no such date {1}.'


def get_category_number(category):
    """
    :param category: name of category
    :return: number of category, mapped
    """
    try:
        return CATEGORIES[category]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(category, AVAILABLE_CATEGORIES))


def get_state_number(state):
    """
    :param state: name of state
    :return: number of state, mapped
    """
    try:
        return STATES[state]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(state, AVAILABLE_STATES))


def get_commodity_number(commodity):
    """
    :param commodity: name of the commodity
    :return: number of commodity, mapped
    """
    try:
        return COMMODITIES[commodity]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(commodity, AVAILABLE_COMMODITIES))


# Need to clean up
def get_date_end(date):
    """
    :param date: 'MMM-YYYY'
    :return: the last date of the month
    """
    date_array = date.split("-")
    month = date_array[0]
    year = date_array[1]

    if month == 'Feb':
        if is_leap_year(int(year)):
            last_feb = '29'
        else:
            last_feb = '28'
        return year + '-02-' + last_feb
    else:
        try:
            return END_DATES[month].format(year=year)
        except KeyError:
            raise LookupNotFoundError(ERROR_FMT.format(month, AVAILABLE_MONTHS))


# Need to clean up
def get_date_end_num(date):
    """
    :param date: 'YYYY-mm-dd'
    :return: the last date of the month
    """
    year, month, _ = date.split("-")

    if month == '02':
        if is_leap_year(int(year)):
            last_feb = '29'
        else:
            last_feb = '28'
        return year + '-02-' + last_feb
    else:
        try:
            return END_DATES_NUM[month].format(year=year)
        except KeyError:
            raise LookupNotFoundError(ERROR_FMT.format(month, AVAILABLE_MONTHS))


def is_leap_year(year):
    """
    :param year: a year
    :return: if it's leap year
    """
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def get_state_name(state_id):
    """
    :param state_id: number
    :return: name of the state
    """
    try:
        return REVERSE_STATES[state_id]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(state_id, AVAILABLE_STATE_IDS))


def reverse_map_categories(category_id):
    """
    :param category_id: number
    :return: name of the category
    """
    try:
        return REVERSE_CATEGORIES[category_id]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(category_id, AVAILABLE_CATEGORY_IDS))


def reverse_map_commodities(commodity_id):
    """
    :param commodity_id: number
    :return: name of the commodity
    """
    try:
        return REVERSE_COMMODITIES[commodity_id]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(commodity_id, AVAILABLE_COMMODITY_IDS))


def get_state_number_retail(state):
    """
    :param state: name
    :return: number of the state
    """
    result = get_state_number(state)
    if result == '-':
        return '0'
    return result


def get_state_number_merch(state):
    """
    :param state: name
    :return: number of the state
    """
    result = get_state_number(state)
    if result == '0':
        return '-'
    return result


def validate_date(start_date, end_date):
    """
    :param start_date: start date
    :param end_date: end date
    :return (start, end): pair of dates
    """
    # because having YYYY-M-DD will pass the datetime strptime
    if start_date:
        if not re.match('^\d{4}-\d{2}-\d{2}$', start_date):
            raise InvalidDateError(DATE_FORMAT_ERROR.format('Start'))
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            raise InvalidDateError(DATE_ERROR.format('Start', start_date))

    if end_date:
        if not re.match('^\d{4}-\d{2}-\d{2}$', end_date):
            raise InvalidDateError(DATE_FORMAT_ERROR.format('End'))
        try:
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise InvalidDateError(DATE_ERROR.format('End', end_date))

    if start_date is None:
        if end_date is None:
            end = datetime.date.today()
            end_date = end.strftime('%Y-%m-%d')
        start = end - relativedelta(months=11)
        start_date = start.strftime('%Y-%m-%d')
    else:
        if end_date is None:
            end = start + relativedelta(months=11)
            end_date = end.strftime('%Y-%m-%d')

    if start > end:
        raise InvalidDateError('Start date should be before end date')

    return start_date, end_date
