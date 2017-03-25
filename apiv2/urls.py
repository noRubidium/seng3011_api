from django.conf.urls import url

from .mock import mock_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^merch/([^/]+)/([^/]+)$', views.showMerchandiseData, name="merch"),
    url(r'^merch/([^/]+)$', views.showMerchandiseData, name="merch"),
    url(r'^retail/([^/]+)/([^/]+)$', views.showRetailData, name="retail"),
    url(r'^retail/([^/]+)', views.showRetailData, name="retail"),
    url(r'^mock/merch/([^/]+)/([^/]+)$', mock_views.showMerchandiseData, name="merch"),
    url(r'^mock/merch/([^/]+)$', mock_views.showMerchandiseData, name="merch"),
    url(r'^mock/retail/([^/]+)/([^/]+)$', mock_views.showRetailData, name="retail"),
    url(r'^mock/retail/([^/]+)', mock_views.showRetailData, name="retail"),
]