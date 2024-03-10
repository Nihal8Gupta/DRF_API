from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CandidateView(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer