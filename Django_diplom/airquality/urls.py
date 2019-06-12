from django.urls import path
from . import views

urlpatterns = [
    path('', views.title_list, name='index'),
]