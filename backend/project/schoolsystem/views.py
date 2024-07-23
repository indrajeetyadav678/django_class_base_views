from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import Departmentmodel, Studentmodel
import json

# Create your views here.


class Studentviews(View):
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if 'id' not in kwargs:
            data = list(Studentmodel.objects.all().values()) 
            return JsonResponse({'data':data}, safe=False)
        else:
            item= get_object_or_404(Studentmodel, id=kwargs['id'])
            res = [item]
            return JsonResponse({'data':res}, safe=False)
    
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            Studentmodel.objects.create(**data)

            res=[{'msg':'data saved successfully'}]
            return JsonResponse({'data':res}, safe=False)
        except:
            token = get_token()
            res=[{'msg':'data saving error'}]
            return JsonResponse({'data':res}, safe=False)

    
    
    def put(self, request, *args, **kwargs):
        if 'id' not in kwargs:
            res=[{'msg':'id not available error'}]
            return JsonResponse({'data':res}, safe=False)
        
        item= get_object_or_404(Studentmodel, id=kwargs['id'])
        data = json.loads(request.body)
        item.name = data['name']
        item.father_name = data['father_name']
        item.classes = data['classes']
        item.fees = data['fees']
        item.fees = data['fees']
        item.save()
        res=[{'msg':'data update successfully'}]
        return JsonResponse({'data':res}, safe=False)
    
    
    def delete(self, request, *args, **kwargs):
        if 'id' not in kwargs:
            res=[{'msg':'id not available error'}]
            return JsonResponse({'data':res}, safe=False)
        
        item= get_object_or_404(Studentmodel, id=kwargs['id'])
        item.delete()
        res=[{'msg':'data delete successfully'}]
        return JsonResponse({'data':res}, safe=False)