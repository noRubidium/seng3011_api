"""
    A lookup table thingy here ( states/category -> number)
"""


class LookupNotFoundError(Exception):
    """
    The error when lookup failed
    """
    def __init__(self, value):
        Exception.__init__(self, value)
        self.value = value

    def __str__(self):
        return repr(self.value)


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
    'NoStateDetails': '9',
    'ReExports': 'F',
    'AUS': '0',
    'NSW': '1',
    'WA': '5',
    'SA': '4',
    'ACT': '8',
    'VIC': '2',
    'TAS': '6',
    'QLD': '3',
    'NT': '7',
    '': '-'
}

AVAILABLE_STATES = STATES.keys()

REVERSE_STATES = {
    '-': 'Total',
    '9': 'NoStateDetails',
    'F': 'ReExports',
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
    :param date: 'Mth-YYYY'
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
    :param state: number
    :return: name of the state
    """
    try:
        return REVERSE_STATES[state_id]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(state_id, AVAILABLE_STATE_IDS))


def reverse_map_categories(category_id):
    """
    :param category: number
    :return: name of the category
    """
    try:
        return REVERSE_CATEGORIES[category_id]
    except KeyError:
        raise LookupNotFoundError(ERROR_FMT.format(category_id, AVAILABLE_CATEGORY_IDS))


def reverse_map_commodities(commodity_id):
    """
    :param commodity: number
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
