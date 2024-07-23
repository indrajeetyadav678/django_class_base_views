from rest_framework import serializers
from .models import Departmentmodel , Studentmodel


class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model = Departmentmodel
        fields = '__all__'


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Studentmodel
        fields = '__all__'