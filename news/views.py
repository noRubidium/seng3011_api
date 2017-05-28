"""
The view layer of the API, handle string beautify and stuff
"""
from django.http import JsonResponse
from .crocs import cross_origin

from .utils import get_news, get_news_detail, get_summary


@cross_origin
def get_company_news(request, company):
    """
    get the request, return news items for the company
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of news related to company
    """
    return JsonResponse(get_news(company))


@cross_origin
def get_news_item_data(request, encoded_url):
    """
    get the request, return data for the news article
    :param request: http request
    :param encoded_url: url of the news article
    :return: JSON of news article data
    """

    return JsonResponse(get_news_detail(encoded_url))


@cross_origin
def get_company_summary(request, company):
    return JsonResponse(get_summary(company))