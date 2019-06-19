from django.conf.urls import url
from django.urls import path

from Django_diplom.airquality import admin
from . import views

urlpatterns = [
    path('', views.viewdata, name='data'),
    #path('', views.view_func, name='view_func')
    url(r'^$', views.home),
    url(r'^data/', views.get_data)
]