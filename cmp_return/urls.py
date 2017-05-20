"""
Manage the URL routing
"""
from django.conf.urls import url

from . import views

urlpatterns = [url(r'^(?P<cmp>.*)/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})$', views.filtered, name='filter'), url(r'^(?P<cmp>.{6})$', views.index, name='index')]
