from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^measurements/', views.MeasurementList),
    url(r'^measurementcreate/$', csrf_exempt(views.MeasurementCreate), name='measurementCreate'),
    url(r'^createmeasurements/$', csrf_exempt(views.MeasurementsCreate), name='createMeasurements'),
]