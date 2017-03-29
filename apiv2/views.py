from django.http import HttpResponse
from utils import get_commodity_number,get_category_number,get_state_number

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")


def showMerchandiseData(request, commodities, states="AUS"):
    startDate = request.GET.get('startDate', 'defaultStartDate')
    endDate = request.GET.get('endDate', 'defaultEndDate')

    commoditiesLine = '+'.join((map(get_commodity_number, commodities.split(','))))
    stateLine = '+'.join((map(get_state_number, states.split(','))))

    absRequest = "MERCH_EXP" + "/" + stateLine + "." #add state
    absRequest += commoditiesLine + "."
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

    categoryLine = '+'.join((map(get_category_number, commodities.split(','))))
    stateLine = '+'.join((map(get_state_number, states.split(','))))

    absRequest = "RT" + "/" + stateLine + "." #add state
    absRequest += "2" + "." #add data type
    absRequest += categoryLine + "."
    absRequest += "10.M" #default adjustment type (10-original) and request monthly data
    absRequest += "/all?startTime=" + startDate + "&endTime=" + endDate
    return HttpResponse("categories: " + categories + " <br>states: " + states + " \
    <br>startDate: " + startDate + " <br>endDate: " + endDate + " <br>absRequest: " + absRequest)

    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response
