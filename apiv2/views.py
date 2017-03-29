from django.http import HttpResponse, JsonResponse
from utils import get_commodity_number, get_category_number, get_state_number
from parse import parse_merchandise, parse_retail
from crocs import cross_origin

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")

@cross_origin
def showMerchandiseData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', None)
    endDate = request.GET.get('endDate', None)

    # String to list
    commodities[] = commodities.split(", ")

    # init a Merchandise Object
    # get the JSON file with the get_data method or something like that
    merch = Merchandise(commodities, states, startDate, endDate)
    # merch.get_data()

    result = parse_merchandise(merch)
    return JsonResponse({"categories":categories, "states":states, "start": startDate, "end": endDate})

@cross_origin
def showRetailData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', None)
    endDate = request.GET.get('endDate', None)

    # String to list
    categories[] = categories.split(",")

    # init a Retail Object
    # get the JSON file with the get_data method or something like that
    retail = Retail(commodities, states, startDate, endDate)
    # retail.get_data()

    result = parse_retail(retail)
    return JsonResponse({"categories":categories, "states":states, "start": startDate, "end": endDate})