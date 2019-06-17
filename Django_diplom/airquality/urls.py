from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewdata, name='data'),
    #path('', views.TableView, name='index1.html'),
]