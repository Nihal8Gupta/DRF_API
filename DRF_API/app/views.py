from django.shortcuts import render
from app.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class EmployeeDetail(APIView):

    def get(self,request):
        obj = Employee.objects.all()
        serializer = EmployeeSerialier(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class EmployeeInfo(APIView):
    def get(self,request,id):
        try:
            obj = Employee.objects.get(Eid=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Does Not Exist'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerialier(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj = Employee.objects.get(Eid=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Does Not Exist'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerialier(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj = Employee.objects.get(Eid=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Does Not Exist'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerialier(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            obj = Employee.objects.get(Eid=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Does Not Exist'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'message':'deleted'},status=status.HTTP_204_NO_CONTENT)