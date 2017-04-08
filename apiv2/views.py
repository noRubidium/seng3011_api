"""
The view layer of the API, handle string beautify and stuff
"""

import datetime
import logging
import time
from django.http import HttpResponse, JsonResponse
from .utils import LookupNotFoundError
from .parse import parse_merchandise, parse_retail
from .crocs import cross_origin
from .models import Merchandise, Retail

# configure logging formatting
logging.basicConfig(filename="all_events.log", level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")

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

    # begin timer and log request
    start_time = time.time()
    logging.info("API request made with url: {}".format(request.get_full_path()))

    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    start_date = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    end_date = request.GET.get('endDate', now.strftime("%Y-%m-%d"))

    # String to list
    categories_list = categories.split(',')
    states_list = states.split(',')

    try:
        merch = Merchandise(categories_list, states_list, start_date, end_date)
    except LookupNotFoundError as error:
        logging.error("HTTP 404: Request '{}': {}".format(request.get_full_path(), error))
        return HttpResponse(str(error), status=404)

    merch_json = merch.get_json()
    if merch.response_status == "error":
        return JsonResponse(merch_json)

    result = parse_merchandise(merch_json)

    # end timer and log successful response
    end_time = time.time()
    ms_elapsed = (start_time - end_time)*1000
    logging.info("HTTP 200: Request '{}' successfully returned. Time taken: {}ms".format(request.get_full_path(), ms_elapsed))

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

    # begin timer and log request
    start_time = time.time()
    logging.info("API request made with url: {}".format(request.get_full_path()))

    now = datetime.datetime.now()
    prev_year = now - datetime.timedelta(days=365)

    start_date = request.GET.get('startDate', prev_year.strftime("%Y-%m-%d"))
    end_date = request.GET.get('endDate', now.strftime("%Y-%m-%d"))

    # String to list
    categories_list = categories.split(',')
    states_list = states.split(',')

    # init a Retail Object
    # get the JSON file with the get_data method or something like that
    try:
        retail = Retail(categories_list, states_list, start_date, end_date)
    except LookupNotFoundError as error:
        logging.error("HTTP 404: Request '{}': {}".format(request.get_full_path(), error))
        return HttpResponse(str(error), status=404)

    retail_json = retail.get_json()
    if retail.response_status == "error":
        return JsonResponse(retail_json)

    result = parse_retail(retail_json)

    # end timer and log successful response
    end_time = time.time()
    ms_elapsed = (start_time - end_time)*1000
    logging.info("HTTP 200: Request '{}' successfully returned. Time taken: {}ms".format(request.get_full_path(), ms_elapsed))
    
    return JsonResponse(result)
