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
        'CafesResturantsAndTakeawayFood': '46',
        'Other': '45'
    }.get(category, category)

def get_state_number(state):
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
    }.get(state, state)

def get_commodity_number(commodity):
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
    }.get(commodity, commodity)
