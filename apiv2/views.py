from django.http import HttpResponse

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")


def showMerchandiseData(request, commodities, states="AUS"):
    startDate = request.GET.get('startDate', 'defaultStartDate')
    endDate = request.GET.get('endDate', 'defaultEndDate')

    absRequest = "MERCH_EXP" + "/" + convertToAbs(states,getStateNumber) + "." #add state
    absRequest += convertToAbs(commodities,getCommodityNumber) + "."
    absRequest += "-1.-.M" #default industry of origin (-1), country of destination (-) and request monthly data (M)
    absRequest += "/all?startTime=" + startDate + "&endTime=" + endDate
    return HttpResponse("commodities: " + commodities + " <br>states: " + states + " \
    <br>startDate: " + startDate + " <br>endDate: " + endDate + " <br>absRequest: " + absRequest)
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response

def showRetailData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', 'defaultStartDate')
    endDate = request.GET.get('endDate', 'defaultEndDate')

    absRequest = "RT" + "/" + convertToAbs(states,getStateNumber) + "." #add state
    absRequest += "2" + "." #add data type
    absRequest += convertToAbs(categories,getCategoryNumber) + "."
    absRequest += "10.M" #default adjustment type (10-original) and request monthly data
    absRequest += "/all?startTime=" + startDate + "&endTime=" + endDate
    return HttpResponse("categories: " + categories + " <br>states: " + states + " \
    <br>startDate: " + startDate + " <br>endDate: " + endDate + " <br>absRequest: " + absRequest)

    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response


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
