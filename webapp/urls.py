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
    url(r'^$', views.get_all_companies),
    url(r'^(?P<company>\w{3}\.\w{2})$', views.get_company_data)
]