"""
The view layer of the API, handle string beautify and stuff
"""
import json
from django.http import HttpResponse, JsonResponse
from .crocs import cross_origin
from .models import RetailData
from .utils import companies_info

@cross_origin
def index(request):
    """
    # Index route, only echo the request
    :param request: http request
    :return: http response
    """
    return HttpResponse('This is the API end point v3. Request is:' + str(request))


@cross_origin
def get_all_companies(request):
    """
    :param request: http request
    :return: JSON of companies
    """
    return JsonResponse({'companies': companies_info})


@cross_origin
def get_company_data(request, company):
    """
    get the request, return retail data
    :param request: http request
    :param company: company string
    :return: JSON of details of company
    """

    retail = retail_data(company)

    return JsonResponse({'jess': 'cool'})
