from django.conf.urls import url

from .mock import mock_views
from . import views

MERCH = "merch"
RETAIL = "retail"

shortUrl = r'{0}/(?P<categories>[^/]+)/$'
longUrl = r'{0}/(?P<categories>[^/]+)/(?P<states>[^/]+)/?$'

def makeRoutingWithMock(name, urlbase):
    def makeRouting(uri, fromModule, methodName):
        return url(uri, getattr(fromModule, methodName))
    def pairMaking(methodName):
        return [makeRouting(r'^' + urlbase.format(name), views, methodName),
                makeRouting(r'^mock/' + urlbase.format(name), mock_views, methodName)]

    if name == MERCH:
        return pairMaking("showMerchandiseData")
    if name == RETAIL:
        return pairMaking("showRetailData")
    return []

urlpatterns = [url(r'^$', views.index, name='index')]  + makeRoutingWithMock(MERCH, shortUrl) \
              + makeRoutingWithMock(MERCH, longUrl) + makeRoutingWithMock(RETAIL, shortUrl) + makeRoutingWithMock(RETAIL, longUrl)