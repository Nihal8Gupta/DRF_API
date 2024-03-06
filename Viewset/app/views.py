from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import *
from rest_framework import status

# Create your views here.
class ProductView(ViewSet):
    def list(self,request):
        allobj = Product.objects.all()
        sobj = ProductSerializer(allobj,many=True)
        return Response(sobj.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk):
        PO = Product.objects.get(pk=pk)
        sobj = ProductSerializer(PO)
        return Response(sobj.data,status=status.HTTP_302_FOUND)

    def create(self,request):
        sobj = ProductSerializer(data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        PO = Product.objects.get(pk=pk)
        sobj = ProductSerializer(PO,data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_202_ACCEPTED)
        return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        PO = Product.objects.get(pk=pk)
        sobj = ProductSerializer(PO,data=request.data,partial=True)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_202_ACCEPTED)
        return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'delete':'object has been deleted !'},status=status.HTTP_200_OK)