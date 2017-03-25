from django.conf.urls import url

from .mock import mock_views
from . import views

merchUrl = r'merch/([^/]+)$'
merchUrlLong = r'merch/([^/]+)/([^/]+)$'
retailUrlLong = r'retail/([^/]+)/([^/]+)$'
retailUrl = r'retail/([^/]+)$'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^' + merchUrl, views.showMerchandiseData, name="merch"),
    url(r'^' + merchUrlLong, views.showMerchandiseData, name="merch"),
    url(r'^' + retailUrl, views.showRetailData, name="retail"),
    url(r'^' + retailUrlLong, views.showRetailData, name="retail"),
    url(r'^mock/' + merchUrlLong, mock_views.showMerchandiseData, name="merch"),
    url(r'^mock/' + merchUrl, mock_views.showMerchandiseData, name="merch"),
    url(r'^mock/' + retailUrlLong, mock_views.showRetailData, name="retail"),
    url(r'^mock/' + retailUrl, mock_views.showRetailData, name="retail"),
]