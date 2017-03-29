from django.http import HttpResponse, JsonResponse
from utils import get_commodity_number,get_category_number,get_state_number
from parse import parse_merchandise, parse_retail
from crocs import cross_origin

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")

@cross_origin
def showMerchandiseData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', None)
    endDate = request.GET.get('endDate', None)

    # init a Merchandise Object (pass in the args needed, look at models.py)
    # get the JSON file with the get_data method or something like that

    # result = parse_merchandise("{}")
    return JsonResponse({"categories":categories, "states":states, "start": startDate, "end": endDate})

@cross_origin
def showRetailData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', None)
    endDate = request.GET.get('endDate', None)

    # init a Retail Object (pass in the args needed, look at models.py)
    # get the JSON file with the get_data method or something like that

    # result = parse_retail("{}")
    return JsonResponse({"categories":categories, "states":states, "start": startDate, "end": endDate})