from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from eclinic_app.models import Patient, PatientRecords, Test

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def assistant_landing_page(request):
    records = PatientRecords.objects.all().order_by('-id')[:5]
    response = []
    for rec in records:
        patient_id = rec.patient_id
        patient = Patient.objects.get(id = patient_id)
        temp_res = {
            "date" : rec.date_time,
            "uid": patient.username,
            "name": patient.name,
            "purpose": rec.purpose
        }
        response.append(temp_res)
    print(response)
    return render(request, 'eclinic_app/AssistantLandingPage.html', {'response': response})
