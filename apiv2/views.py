from django.http import HttpResponse

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")


def showMerchandiseData(request, categories, states="AUS"):
    return HttpResponse("This is the API end point v2.")
    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response

def showRetailData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', 'defaultStartDate')
    endDate = request.GET.get('endDate', 'defaultEndDate')
    absRequest = "RT" + "/" + convertStates(states) + "." #add state
    absRequest += "2" + "." #add data type
    absRequest += convertCategories(categories) + "."
    absRequest += "10.M" #default adjustment type (10-original) and request monthly data
    absRequest += "/all?startTime=" + startDate + "&endTime=" + endDate
    print absRequest
    return HttpResponse("categories: " + categories + " <br>states: " + states + " \
    <br>startDate: " + startDate + " <br>endDate: " + endDate + " <br>absRequest: " + absRequest)

    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response

def convertStates(states):
    splitStates = [x.strip() for x in states.split(',')]
    convertedString = ""
    for state in splitStates:
        convertedString += getStateNumber(str(state)) + "+"
    return convertedString[:-1]

def convertCategories(categories):
    splitCategories = [x.strip() for x in categories.split(',')]
    convertedString = ""
    for category in splitCategories:
        convertedString += getCategoryNumber(str(category)) + "+"
    return convertedString[:-1]

def getCategoryNumber(category):
    return {
        'Total': '20',
        'Food': '41',
        'HousholdGood': '42',
        'ClothingFootwareAndPersonalAccessory': '43',
        'DepartmentStores': '44',
        'CafesResturantsAndTakeawayFood': '46',
        'Other': '45'
    }.get(category, 'NA')

def getStateNumber(state):
    return {
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
