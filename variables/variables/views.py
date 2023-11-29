from .models import Variable
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def VariableList(request):
    queryset = Variable.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def VariableCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        variable = Variable()
        variable.name = data_json["name"]
        variable.save()
        return HttpResponse("successfully created variable")