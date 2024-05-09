from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
import csv
# Create your views here.


class HomeView(APIView):
    def get(self, request):
        return render(request, 'index.html')
        

    # template_name = "index.html"
    # context = {}

class AutoVCView(APIView):
    def get(self, request):
        return render(request, 'autovc.html')
    # template_name = "autovc.html"
    # context = {}

class StarGanView(TemplateView):
    template_name = "starGan.html"
    # context = {}

class kNNView(TemplateView):
    template_name = "knn.html"
    # context = {}

class ResultsView(TemplateView):
    template_name = "results.html"
    with open('results.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    # data = list(data)
    # result = template.render(data=data)
    # data_html = data.to_html() 
    extra_context = {'data': data[1:]}

    # print(data)
    # context = {}