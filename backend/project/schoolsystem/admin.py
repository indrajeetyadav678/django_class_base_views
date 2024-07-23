from django.contrib import admin
from .models import Studentmodel, Departmentmodel

# Register your models here.


admin.site.register(Studentmodel)
admin.site.register(Departmentmodel)