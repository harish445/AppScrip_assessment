from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from .models import Nurse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create Nurse

@method_decorator(csrf_exempt, name='dispatch')  
class CreateNurse(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('name')

        product_data = {
            'name': p_name,
        }

        nurse = Nurse.objects.create(**product_data)

        data = {
            "message": f"New nurse created with id: {nurse.id}"
        }
        return JsonResponse(data, status=201)

    # get all Nurse
    def get(self, request):
        items_count = Nurse.objects.count()
        items = Nurse.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'name': item.name,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)
    
    
# Update Nurse

@method_decorator(csrf_exempt, name='dispatch')
class NurseUpdate(View):
    
    def patch(self, request, nurse_id):
        data = json.loads(request.body.decode("utf-8"))
        item = Nurse.objects.get(id=nurse_id)
        item.name = data['name']
        item.save()

        data = {
            'message': f'Nurse {nurse_id} has been updated'
        }

        return JsonResponse(data)
    
    # Delete a Nurse
    
    def delete(self, request, nurse_id):
        item = Nurse.objects.get(id=nurse_id)
        item.delete()

        data = {
            'message': f'Nurse with id: {nurse_id} has been deleted'
        }

        return JsonResponse(data)
    
    
def getRoutes(request):
    routes = {
        # API's for NURSE
        'get' : '/create-nurse/',
        'post' : '/create-nurse/',
        'patch' : '/create-nurse/id',
        'delete' : '/create-nurse/id',
        'GET' : '/appointment/create-appointment/',
        'GET' : '/appointment/get-appointment/',
        'PATCH' : '/appointment/update-appointment/id',
        'DELETE' : '/appointment/update-appointment/id',
        'POST' : '/appointment/create-appointment/',
    }

    return JsonResponse(routes)
    
