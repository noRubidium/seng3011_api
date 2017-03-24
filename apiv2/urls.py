from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Add proper routing to the view
    # doc should be in Django website
]