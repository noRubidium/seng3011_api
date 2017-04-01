from django.conf.urls import url
from django.http import HttpResponse
from crocs import cross_origin

from .mock import mock_views
from . import views

MERCH = "MerchandiseExports"
RETAIL = "Retail"

shortUrl = r'{0}/(?P<categories>[A-Za-z,]+)/?$'
longUrl = r'{0}/(?P<categories>[A-Za-z,]+)/(?P<states>[A-Za-z,]+)/?$'

'''
    Make a pair of routing and the corresponding test routing
    :param name: name of the routing
    :param urlbase: the url formatting regex
    :return a list of two url matching
'''

def make_routing_with_mock(name, urlbase):
    def make_routing(uri, from_module, method_name):
        return url(uri, getattr(from_module, method_name)) # getattr takes method out of the module

    def pair_making(method_name):
        return [make_routing(r'^' + urlbase.format(name), views, method_name),
                make_routing(r'^mock/' + urlbase.format(name), mock_views, method_name)]

    if name == MERCH:
        return pair_making("show_merchandise_data")
    if name == RETAIL:
        return pair_making("show_retail_data")
    return []

@cross_origin
def not_found(request):
    return HttpResponse("Please do not try to brute force traverse all the url!", status=404)

urlpatterns = [url(r'^$', views.index, name='index')] \
              + make_routing_with_mock(MERCH, shortUrl) \
              + make_routing_with_mock(MERCH, longUrl) \
              + make_routing_with_mock(RETAIL, shortUrl) \
              + make_routing_with_mock(RETAIL, longUrl)\
              + [url(r'.', not_found)]
              