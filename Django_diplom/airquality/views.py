import json

from django.http import JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from Django_diplom.airquality.models import Airdata


def home(request):
    return render(request, 'index.html')


def viewdata(request):
        data = Airdata.objects.all()
        return TemplateResponse(request, 'index.html', {'data': data})


def get_data(request):
    data = {
        'DateT': ['2019-06-10 12:00:00', '2019-06-10 18:00:00', '2019-06-11 06:00:00', '2019-06-11 12:00:00', '2019-06-11 18:00:00', '2019-06-12 06:00:00', '2019-06-12 12:00:00', '2019-06-12 18:00:00',
                  '2019-06-13 06:00:00', '2019-06-13 12:00:00', '2019-06-13 18:00:00', '2019-06-14 06:00:00', '2019-06-14 12:00:00', '2019-06-14 18:00:00', '2019-06-15 06:00:00', '2019-06-15 12:00:00',
                  '2019-06-16 06:00:00', '2019-06-16 06:00:00', '2019-06-16 12:00:00', '2019-06-16 18:00:00', '2019-06-17 06:00:00', '2019-06-17 12:00:00', '2019-06-17 18:00:00', '2019-06-18 06:00:00',
                  '2019-06-18 12:00:00', '2019-06-18 18:00:00', '2019-06-19 06:00:00', '2019-06-19 12:00:00', '2019-06-19 18:00:00', '2019-06-20 06:00:00'],
        'PM25': [17, 27, 14, 20, 28, 16, 22, 32, 13, 17, 27, 9, 15, 35, 21, 27, 30, 15, 21, 32, 11, 19, 26, 8, 15, 25, 5, 21, 30, 9],
        'Allowed': [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
    }
    return JsonResponse(data)