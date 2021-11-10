from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import TempInto, TempintoFile
from .serializers import TempIntoSerializer, TempintoFileSerializer


class TempIntoViewSet(viewsets.ModelViewSet):
    queryset = TempInto.objects.all()
    serializer_class = TempIntoSerializer


class TempintoFileViewSet(viewsets.ModelViewSet):
    queryset = TempintoFile.objects.all()
    serializer_class = TempintoFileSerializer
