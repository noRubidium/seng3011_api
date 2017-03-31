# A lookup table thingy here ( states/category -> number)


class LookupNotFoundError(Exception):
    def __init__(self, value):
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



def get_category_number(category):
    try:
        return CATEGORIES[category]
    except KeyError as e:
        raise LookupNotFoundError('The type you are requiring ({0}) doesn\'t exist. You should choose from {1}'
                        .format(category,AVAILABLE_CATEGORIES))

def get_state_number(state):
    try:
        return STATES[state]
    except KeyError as e:
        raise LookupNotFoundError('The type you are requiring ({0}) doesn\'t exist.  You should choose from {1}'
                        .format(state, AVAILABLE_STATES))


def get_commodity_number(commodity):
    try:
        return COMMODITIES[commodity]
    except KeyError as e:
        raise LookupNotFoundError('The type you are requiring ({0}) doesn\'t exist.  You should choose from {1}'
                        .format(commodity, AVAILABLE_COMMODITIES))


def get_state_name(state):
    return {
        '-': 'Total',
        '9': 'NoStateDetails',
        'F': 'ReExports',
        '0': 'Australia',
        '1': 'New South Wales',
        '5': 'Western Australia',
        '4': 'South Australia',
        '8': 'Australia Capital Territory',
        '2': 'Victoria',
        '6': 'Tasmania',
        '3': 'Queensland',
        '7': 'Northern Territory'
    }.get(state, state)

def get_state_abbrev_from_id(state):
    return {
        '-': 'AUS',
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
    }.get(state, state)


def get_state_abbrev(state):
    return {
        '-': 'Total',
        '9': 'NoStateDetails',
        'F': 'ReExports',
        'Whole Australia': 'AUS',
        'New South Wales': 'NSW',
        'Western Australia': 'WA',
        'South Australia': 'SA',
        'Australian Capital Territory': 'ACT',
        'Victoria': 'VIC',
        'Tasmania': 'TAS',
        'Queensland': 'QLD',
        'Northern Territory': 'NT'
    }.get(state, state)


# Need to clean up
def get_date_end(date):
    date_array = date.split("-")
    month = date_array[0]
    year = date_array[1]

    if is_leap_year(int(year)):
        last_feb = '29'
    else:
        last_feb = '28'

    return {
        'Jan': year + '-01-31',
        'Feb': year + '-02-' + last_feb,
        'Mar': year + '-03-31',
        'Apr': year + '-04-30',
        'May': year + '-05-31',
        'Jun': year + '-06-30',
        'Jul': year + '-07-31',
        'Aug': year + '-08-31',
        'Sep': year + '-09-30',
        'Oct': year + '-10-31',
        'Nov': year + '-11-30',
        'Dec': year + '-12-31',
    }.get(month, date)


def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def reverse_map_categories(category):
    return REVERSE_CATEGORIES[category]


def reverse_map_commodities(commodity):
    return REVERSE_COMMODITIES[commodity]


def get_state_number_retail(state):
    result = get_state_number(state)
    if result == '-':
        return '9'
    return result


def get_state_number_merch(state):
    result = get_state_number(state)
    if result == '9':
        return '-'
    return result