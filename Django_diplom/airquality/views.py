from django.shortcuts import render
from django.template.response import TemplateResponse

from Django_diplom.airquality.models import Airdata


def viewdata(request):
        data = Airdata.objects.all()
        return TemplateResponse(request, 'index.html', {'data': data})

