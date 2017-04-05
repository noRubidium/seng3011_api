"""
The view layer of the API, handle string beautify and stuff
"""

import datetime
from django.http import HttpResponse, JsonResponse
from .utils import LookupNotFoundError, InvalidDateError, validate_date
from .parse import parse_merchandise, parse_retail
from .crocs import cross_origin
from .models import Merchandise, Retail

@cross_origin
def index(request):
    """
    # Index route, only echo the request
    :param request: http request
    :return: http response
    """
    return HttpResponse("This is the API end point v2. Request is:" + str(request))


@cross_origin
def show_merchandise_data(request, categories, states="Total"):
    """
    get the request, return merchandise data
    :param request: contain date
    :param categories: Categories string
    :param states: str, List of states
    :return: JSON of merch data
    """
    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    start_date = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    end_date = request.GET.get('endDate', now.strftime("%Y-%m-%d"))

    try:
        validate_date(start_date, end_date)
    except InvalidDateError as error:
        return JsonResponse(error.to_json(), status=404)

    # string to list
    categories_list = categories.split(',')
    states_list = states.split(',')

    try:
        merch = Merchandise(categories_list, states_list, start_date, end_date)
    except LookupNotFoundError as error:
        return JsonResponse(error.to_json(), status=404)

    merch_json = merch.get_json()
    if merch.response_status == "error":
        return JsonResponse(merch_json)

    result = parse_merchandise(merch_json)
    return JsonResponse(result)


@cross_origin
def show_retail_data(request, categories, states="AUS"):
    """
    get the request, return retail data
    :param request: contain date
    :param categories: Categories string
    :param states: str, List of states
    :return: JSON of retail data
    """
    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    start_date = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    end_date = request.GET.get('endDate', now.strftime("%Y-%m-%d"))

    try:
        validate_date(start_date, end_date)
    except InvalidDateError as error:
        return JsonResponse(error.to_json(), status=404)

    # string to list
    categories_list = categories.split(',')
    states_list = states.split(',')

    # init a Retail Object
    # get the JSON file with the get_data method or something like that
    try:
        retail = Retail(categories_list, states_list, start_date, end_date)
    except LookupNotFoundError as error:
        return JsonResponse(error.to_json(), status=404)

    retail_json = retail.get_json()
    if retail.response_status == "error":
        return JsonResponse(retail_json)

    result = parse_retail(retail_json)
    return JsonResponse(result)
