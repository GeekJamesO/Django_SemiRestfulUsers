from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new$', views.new),
    url(r'^create$', views.create),  # Post method sends here..
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy),
    url(r'^update$', views.update),
    url(r'^(?P<number>\d+)/$', views.show),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^$', views.index),
]
