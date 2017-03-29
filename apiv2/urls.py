from django.conf.urls import url
from django.http import HttpResponse

from .mock import mock_views
from . import views

MERCH = "merch"
RETAIL = "retail"

shortUrl = r'{0}/(?P<categories>[A-Za-z]+)/?$'
longUrl = r'{0}/(?P<categories>[A-Za-z]+)/(?P<states>[A-Za-z]+)/?$'


def make_routing_with_mock(name, urlbase):
    def make_routing(uri, from_module, method_name):
        return url(uri, getattr(from_module, method_name))

    def pair_making(method_name):
        return [make_routing(r'^' + urlbase.format(name), views, method_name),
                make_routing(r'^mock/' + urlbase.format(name), mock_views, method_name)]

    if name == MERCH:
        return pair_making("showMerchandiseData")
    if name == RETAIL:
        return pair_making("showRetailData")
    return []


def not_found(request):
    return HttpResponse("Please do not try to brute force traverse all the url!", status=404)

urlpatterns = [url(r'^$', views.index, name='index')] \
              + make_routing_with_mock(MERCH, shortUrl) \
              + make_routing_with_mock(MERCH, longUrl) \
              + make_routing_with_mock(RETAIL, shortUrl) \
              + make_routing_with_mock(RETAIL, longUrl)\
              + [url(r'.', not_found)]