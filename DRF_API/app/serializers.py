from rest_framework import serializers
from app.serializers import *
from .models import Employee

# ModelSerializer
class EmployeeSerialier(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
