from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from .models import Appointment, Nurse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# import pymongo
# from pymongo import MongoClient

# client = pymongo.MongoClient("mongodb+srv://harish:Harish4455@appscrip.qobzbv6.mongodb.net/?retryWrites=true&w=majority")

# db = client['nurse_management']
# collection = db['nurses']

@method_decorator(csrf_exempt, name='dispatch')
class CreateNurseAppointment(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        p_nurse = data.get('name')
        p_name = data.get('appoint')
        p_appoint = data.get('is_appoint')

        nurse_data = {
            'name': p_name,
            'appoint': p_name,
            'is_appoint': p_appoint,
        }

        nurse = Appointment.objects.create(**nurse_data)

        data = {
            "message": f"Appointment created for nurse with id: {nurse.id}"
        }
        return JsonResponse(data, status=201)


    # get number of nurses without any appointment
    
    def get(self, request):
        
        items_count = Appointment.objects.count()
        items = Appointment.objects.filter(is_appoint='False')

        items_data = []
        for item in items:
            items_data.append({
                'appoint': item.is_appoint,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)
    
# get number of nurses with appointment

@method_decorator(csrf_exempt, name='dispatch')
class GetAppointNurse(View):
    def get(self, request):
        
        items_count = Appointment.objects.filter(is_appoint='True').count()
        items = Appointment.objects.filter(is_appoint='True')

        items_data = []
        for item in items:
            items_data.append({
                'appoint': item.is_appoint,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)

# update appointment os a nurse

@method_decorator(csrf_exempt, name='dispatch')
class AppointmentUpdate(View):
    
    def patch(self, request, appoint_id):
        data = json.loads(request.body.decode("utf-8"))
        item = Appointment.objects.get(id=appoint_id)
        #item.appoint = data['appoint']
        item.is_appoint = data['is_appoint']
        item.save()

        data = {
            'message': f'Appointment with id {appoint_id} has been updated'
        }

        return JsonResponse(data)
    
    # delete appointment
    
    def delete(self, request, appoint_id):
        item = Appointment.objects.get(id=appoint_id)
        item.delete()

        data = {
            'message': f'Appointment with id: {appoint_id} has been deleted'
        }

        return JsonResponse(data)
    
