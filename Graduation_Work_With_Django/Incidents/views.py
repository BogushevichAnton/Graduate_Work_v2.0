from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def Incidents(request):
    return HttpResponse("Страница всех Incidents")

def IncidentsID(request, IncidentId):
    print(request.GET)
    return HttpResponse(f"Страница конкретного Incident <p>{IncidentId}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница инцидентов не найдена')