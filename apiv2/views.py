from django.http import HttpResponse, JsonResponse
from utils import get_commodity_number, get_category_number, get_state_number
from parse import parse_merchandise, parse_retail
from crocs import cross_origin
from models import Merchandise, Retail
import datetime

def index(request):
    return HttpResponse("This is the API end point v2.")

@cross_origin
def show_merchandise_data(request, categories, states="Total"):
    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    start_date = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    end_date = request.GET.get('endDate', now.strftime("%Y-%m-%d"))

    categories_list = categories.split(',')
    states_list = states.split(',')
    
    merch = Merchandise(categories_list, states_list, start_date, end_date)
    merch_json = merch.get_JSON()

    if merch.response_status == "error":
        return JsonResponse(merch_json)
    
    result = parse_merchandise(merch_json)
    return JsonResponse(result)


@cross_origin
def show_retail_data(request, categories, states="AUS"):
    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    start_date = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    end_date = request.GET.get('endDate', now.strftime("%Y-%m-%d"))

    # String to list
    categories_list = categories.split(',')
    states_list = states.split(',')

    retail = Retail(categories_list, states_list, start_date, end_date)
    retail_json = retail.get_JSON()

    if retail.response_status == "error":
        return JsonResponse(retail_json)

    result = parse_retail(retail_json)
    return JsonResponse(result)
