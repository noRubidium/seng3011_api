from django.http import HttpResponse, JsonResponse
from utils import get_commodity_number, get_category_number, get_state_number, LookupNotFoundError
from parse import parse_merchandise, parse_retail
from crocs import cross_origin
from models import Merchandise, Retail
import datetime


# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")


@cross_origin
def showMerchandiseData(request, categories, states="Total"):
    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    startDate = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    endDate = request.GET.get('endDate', now.strftime("%Y-%m-%d"))


    # String to list
    categories_list = categories.split(',')
    states_list = states.split(',')
    # init a Merchandise Object
    # get the JSON file with the get_data method or something like that
    try:
        merch = Merchandise(categories_list, states_list, startDate, endDate)
    except LookupNotFoundError as e:
        return HttpResponse(str(e), status=404)
    # merch.get_data()
    j = merch.get_JSON()
    if merch.response_status == "error":
        return JsonResponse(j)
    result = parse_merchandise(j)

    # {"categories":categories, "states":states, "start": startDate, "end": endDate}
    return JsonResponse(result)


@cross_origin
def showRetailData(request, categories, states="AUS"):
    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    startDate = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    endDate = request.GET.get('endDate', now.strftime("%Y-%m-%d"))

    # String to list
    categories_list = categories.split(',')
    states_list = states.split(',')

    # init a Retail Object
    # get the JSON file with the get_data method or something like that
    try:
        retail = Retail(categories_list, states_list, startDate, endDate)
    except LookupNotFoundError as e:
        return HttpResponse(str(e), status=404)
    # retail.get_data()
    j = retail.get_JSON()
    if retail.response_status == "error":
        return JsonResponse(j)
    result = parse_retail(j)
    # return JsonResponse({"categories":categories, "states":states, "start": startDate, "end": endDate})
    return JsonResponse(result)
