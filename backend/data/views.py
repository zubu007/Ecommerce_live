from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DataSerializer
from .models import Data

# Create your views here.
class DataView(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()