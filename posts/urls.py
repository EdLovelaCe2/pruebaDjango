from django.conf.urls import url
from django.contrib import admin
from . import views as view

urlpatterns = [
    url(r'^$', view.post_list, name='list'),
    url(r'^create/$', view.post_create, name='create'),
    url(r'^detail/$', view.post_detail, name='detail'),
    url(r'^update/$', view.post_update, name='update'),
    url(r'^delete/$', view.post_delete, name='delete'),
]
