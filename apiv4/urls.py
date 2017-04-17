"""
Manage the URL routing
"""
from django.conf.urls import url
from django.http import JsonResponse

from .crocs import cross_origin
from .mock import mock_views
from . import views

MERCH = 'MerchandiseExports'
RETAIL = 'Retail'

SHORT_URL = r'{0}/(?P<categories>[A-Za-z,]+)/?$'
LONG_URL = r'{0}/(?P<categories>[A-Za-z,]+)/(?P<states>[A-Za-z,]+)/?$'


def make_routing_with_mock(name, urlbase):
    """
        Make a pair of routing and the corresponding test routing
        :param name: name of the routing
        :param urlbase: the url formatting regex
        :return a list of two url matching
    """
    def make_routing(uri, from_module, method_name):
        """
        Make a routing
        :param uri: url of the thing
        :param from_module: the module of the view gen method
        :param method_name: view gen method name
        :return: a url pattern
        """
        return url(uri, getattr(from_module, method_name)) # getattr takes method out of the module

    def pair_making(method_name):
        """
        make a pair of routing, both mock and real
        :param method_name: name of the method
        :return: pair of routing
        """
        return [make_routing(r'^' + urlbase.format(name), views, method_name),
                make_routing(r'^mock/' + urlbase.format(name), mock_views, method_name)]

    if name == MERCH:
        return pair_making('show_merchandise_data')
    if name == RETAIL:
        return pair_making('show_retail_data')
    return []

@cross_origin
def not_found(_):
    """
    Return the json response of errror
    :param _: None
    :return: Return error
    """
    return JsonResponse({'error': 'You should choose the type and categories. Type is either Retail or MerchandiseExports'}, status=404)

urlpatterns = [url(r'^$', views.index, name='index')]
urlpatterns += make_routing_with_mock(MERCH, SHORT_URL) \
              + make_routing_with_mock(MERCH, LONG_URL) \
              + make_routing_with_mock(RETAIL, SHORT_URL) \
              + make_routing_with_mock(RETAIL, LONG_URL)\
              + [url(r'.', not_found)]
