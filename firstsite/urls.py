"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include('apiv1.urls')),
    url(r'^v1.1/', include('apiv1-1.urls')),
    url(r'^v2/', include('apiv2.urls')),
    url(r'^v3/', include('apiv3.urls')),
    url(r'^v4/', include('apiv4.urls')),
    url(r'^v5/', include('apiv5.urls')),
    url(r'^rapper/', include('wrapper.urls')),
    url(r'^companies/', include('webapp.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^cmp/', include('cmp_return.urls')),
]
