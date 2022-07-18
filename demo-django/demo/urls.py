from django.urls import path
from django.contrib import admin
from .views import attrs, index, metadata
admin.autodiscover()

urlpatterns = [
    path(r'^$', index, name='index'),
    path(r'^attrs/$', attrs, name='attrs'),
    path(r'^metadata/$', metadata, name='metadata'),
]
