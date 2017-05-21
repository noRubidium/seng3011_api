"""
The view layer of the API, handle string beautify and stuff
"""
import json
from django.http import JsonResponse
from .crocs import cross_origin

import urllib2
from .utils import industries, companies


@cross_origin
def get_company_industries(request, company):
    """
    get the request, return industries the company belongs to
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of industries related to company
    """

    response = {'industries': industries[company]}

    return JsonResponse(response)

@cross_origin
def get_industry_companies(request, industry):
    """
    get the request, return companies belonging to the industry
    :param request: http request
    :param company: industry string
    :return: JSON of companies inside industry
    """

    response = {'companies': companies[industry]}

    return JsonResponse(response)

@cross_origin
def get_related_companies(request, company):
    """
    get the request, return industries the company belongs to
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of industries related to company
    """

    related_companies = list()
    for i in industries[company]:
        for c in companies[i]:
            if c != company and c != related_companies:
                related_companies.append(c)

    related_companies.sort()
    response = {'related_companies': related_companies}

    return JsonResponse(response)
