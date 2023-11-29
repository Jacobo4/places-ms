from .models import Measurement
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json
import os

def check_variable(data):
    r = requests.get(os.environ.get('URL_VARIABLES'), headers={"Accept": "application/json"})
    variables = r.json()
    for variable in variables:
        if data["variable"] == variable["id"]:
            return True
    return False

def check_place(data):
    r = requests.get(os.environ.get('URL_PLACES'), headers={"Accept": "application/json"})
    places = r.json()
    for place in places:
        if data["place"] == place["name"]:
            return True
    return False

def MeasurementList(request):
    queryset = Measurement.objects.all()
    context = list(queryset.values('id', 'variable', 'value', 'unit', 'place', 'dateTime'))
    return JsonResponse(context, safe=False)

def MeasurementCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_variable(data_json) == False:
            return HttpResponse("unsuccessfully created measurement. Variable does not exist")
        elif check_place(data_json) == False:
            return HttpResponse("unsuccessfully created measurement. Place does not exist")
        else:
            measurement = Measurement()
            measurement.variable = data_json['variable']
            measurement.value = data_json['value']
            measurement.unit = data_json['unit']
            measurement.place = data_json['place']
            measurement.save()
            return HttpResponse("successfully created measurement")

def MeasurementsCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        measurement_list = []
        for measurement in data_json:
            if check_variable(measurement) == False:
                return HttpResponse("unsuccessfully created measurement. Variable does not exist")
            elif check_place(measurement) == False:
                return HttpResponse("unsuccessfully created measurement. Place does not exist")
            else:
                db_measurement = Measurement()
                db_measurement.variable = measurement['variable']
                db_measurement.value = measurement['value']
                db_measurement.unit = measurement['unit']
                db_measurement.place = measurement['place']
                measurement_list.append(db_measurement)
        
        Measurement.objects.bulk_create(measurement_list)
        return HttpResponse("successfully created measurements")