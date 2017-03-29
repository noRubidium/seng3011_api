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
        'CrudeMaterialAndInedible': '2',
        'MineralFuelLubricantAndRelatedMaterial': '3',
        'AnimalAndVegetableOilFatAndWaxes': '4',
        'ChemicalsAndRelatedProducts': '5',
        'ManufacturedGoods': '6',
        'MachineryAndTransportEquipments': '7',
        'OtherManufacturedArticles': '8',
        'Unclassified': '9'
    }.get(commodity, commodity)
