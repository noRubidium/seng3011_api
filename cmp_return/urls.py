"""
Manage the URL routing
"""
from django.conf.urls import url

from . import views

urlpatterns = [url(r'^(?P<cmp>.*)$', views.index, name='index')]
