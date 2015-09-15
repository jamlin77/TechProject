__author__ = 'Jamison'
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^TechApp/', include('TechApp.urls', namespace= "TechApp")),
    url(r'^admin/', include(admin.site.urls)),
]