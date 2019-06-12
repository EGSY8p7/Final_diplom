import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

#with open('templates/aqi.json') as d:
    #data = json.load(d)

#def load_json_table_format (request):
   # print(data)
    #html = render_to_string()
    #return  HttpResponse({'d': d}, 'Django_diplom/templates/index.html', content_type="application/html")
#return JsonResponse(data, safe=False,content_type="application/html")
#return render(request, 'demoApp/demo.html', {'d': data}, content_type="application/html")

def title_list(request):
    return render(request, 'index.html', {})