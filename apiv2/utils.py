# A lookup table thingy here ( states/category -> number)
def lookup(something):
    return something


def convertToAbs(string,lookup):
    splitCategories = [x.strip() for x in string.split(',')]
    convertedString = ""
    for category in splitCategories:
        convertedString += lookup(str(category)) + "+"
    return convertedString[:-1]

def getCategoryNumber(category):
    return {
        'Total': '20',
        'Food': '41',
        'HouseholdGood': '42',
        'ClothingFootwareAndPersonalAccessory': '43',
        'DepartmentStores': '44',
        'CafesResturantsAndTakeawayFood': '46',
        'Other': '45'
    }.get(category, 'NA')

def getStateNumber(state):
    return {
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
        'NT': '7'
    }.get(state, 'NA')

def getCommodityNumber(category):
    return {
        'Total': '-1',
        'FoodAndLiveAnimals': '0',
        'BeveragesAndTobacco': '1',
        'CrudMaterialAndInedible': '2',
        'MineralFuelLubricentAndRelatedMaterial': '3',
        'AnimalAndVegitableOilFatAndWaxes': '4',
        'ChemicalsAndRelatedProducts': '5',
        'ManufacutedGoods': '6',
        'MachineryAndTransportEquipments': '7',
        'OtheranucacturedArticles': '8',
        'Unclassified': '9'
    }.get(category, 'NA')
