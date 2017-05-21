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
    url(r'^cmp/(?P<company>\w{3})$', views.get_company_industries),
    url(r'^ind/(?P<industry>\w*)$', views.get_industry_companies),
    url(r'^rel/(?P<company>\w{3})$', views.get_related_companies)
]
