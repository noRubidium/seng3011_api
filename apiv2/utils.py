# A lookup table thingy here ( states/category -> number)
def lookup(something):
    return something


def get_category_number(category):
    return {
        'Total': '20',
        'Food': '41',
        'HouseholdGood': '42',
        'ClothingFootwareAndPersonalAccessory': '43',
        'DepartmentStores': '44',
        'CafesRestaurantsAndTakeawayFood': '46',
        'other': '45'
    }.get(category, category)


def get_state_number(state):
    return {
        'Total': '-',
        'NoStateDetails': '9',
        'ReExports': 'F',
        'AUS': '-',
        'NSW': '1',
        'WA': '5',
        'SA': '4',
        'ACT': '8',
        'VIC': '2',
        'TAS': '6',
        'QLD': '3',
        'NT': '7'
    }.get(state, state)


def get_commodity_number(commodity):
    return {
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
    }.get(commodity, commodity)


def get_state_name(state):
    return {
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
    dateArray = date.split("-")
    return {
        'Jan':'31-Jan-' + dateArray[1],
        'Feb':'28-Feb-' + dateArray[1],
        'Mar':'31-Mar-' + dateArray[1],
        'Apr':'30-Apr-' + dateArray[1],
        'May':'31-May-' + dateArray[1],
        'Jun':'30-Jun-' + dateArray[1],
        'Jul':'31-Jul-' + dateArray[1],
        'Aug':'31-Aug-' + dateArray[1],
        'Sep':'30-Sep-' + dateArray[1],
        'Oct':'31-Oct-' + dateArray[1],
        'Nov':'30-Nov-' + dateArray[1],
        'Dec':'31-Dec-' + dateArray[1],
    }.get(dateArray[0], date)


