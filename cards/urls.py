from django.conf.urls import include, url
from django.contrib import admin,auth


from .views import index, register

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/', register)
    
]