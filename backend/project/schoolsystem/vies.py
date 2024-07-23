from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views import View
from .models import Studentmodel  # Adjust the import based on your project structure
from django.views.decorators.csrf import csrf_exempt 
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
class Studentviews(View):
    @method_decorator(csrf_exempt)
    # @csrf_exempt
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if 'id' not in kwargs:
            data = list(Studentmodel.objects.all().values())  # Convert queryset to list of dicts
            return JsonResponse({'data': data}, safe=False)
        else:
            item = get_object_or_404(Studentmodel, id=kwargs['id'])
            res = {'id': item.id, 'name': item.name, 'father_name': item.father_name, 'classes': item.classes, 'fees': item.fees}
            return JsonResponse({'data': res}, safe=False)
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(data)
            student = Studentmodel.objects.create(**data)
            res = {'msg': 'Data saved successfully', 'id': student.id}
            return JsonResponse({'data': res}, safe=False)
        except Exception as e:
            res = {'msg': 'Data saving error', 'error': str(e)}
            return JsonResponse({'data': res}, status=400, safe=False)

    def put(self, request, *args, **kwargs):
        if 'id' not in kwargs:
            res = {'msg': 'ID not available error'}
            return JsonResponse({'data': res}, status=400, safe=False)

        item = get_object_or_404(Studentmodel, id=kwargs['id'])
        try:
            data = json.loads(request.body)
            item.name = data['name']
            item.father_name = data['father_name']
            item.classes = data['classes']
            item.fees = data['fees']
            item.save()
            res = {'msg': 'Data updated successfully'}
            return JsonResponse({'data': res}, safe=False)
        except Exception as e:
            res = {'msg': 'Data updating error', 'error': str(e)}
            return JsonResponse({'data': res}, status=400, safe=False)

    def delete(self, request, *args, **kwargs):
        if 'id' not in kwargs:
            res = {'msg': 'ID not available error'}
            return JsonResponse({'data': res}, status=400, safe=False)

        item = get_object_or_404(Studentmodel, id=kwargs['id'])
        item.delete()
        res = {'msg': 'Data deleted successfully'}
        return JsonResponse({'data': res}, safe=False)
