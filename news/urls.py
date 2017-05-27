"""
Manage the URL routing
"""
from django.conf.urls import url
from django.http import JsonResponse

from .crocs import cross_origin
from . import views


@cross_origin
def not_found(_):
    """
    Return the json response of errror
    :param _: None
    :return: Return error
    """
    return JsonResponse({'error': 'not found'}, status=404)

urlpatterns = [
    url(r'^cmp/(?P<company>\w{3})$', views.get_company_news),
    url(r'^lnk/(?P<encoded_url>.*=)$', views.get_news_item_data)
]
