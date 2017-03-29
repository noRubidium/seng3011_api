from django.http import HttpResponse
from utils import get_commodity_number,get_category_number,get_state_number

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")


def showMerchandiseData(request, commodities, states="AUS"):
    startDate = request.GET.get('startDate', None)
    endDate = request.GET.get('endDate', None)

    # init a Merchandise Object (pass in the args needed, look at models.py)
    # get the JSON file with the get_data method or something like that

    # result = parse_merchandise(jsonfile)
    # return JsonResponse(result)

def showRetailData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', None)
    endDate = request.GET.get('endDate', None)

    # init a Retail Object (pass in the args needed, look at models.py)
    # get the JSON file with the get_data method or something like that

    # result = parse_commodity(jsonfile)
    # return JsonResponse(result)
