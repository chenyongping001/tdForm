from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import TempInto, TempintoFile
from .serializers import TempIntoSerializer, TempintoFileSerializer


class TempIntoViewSet(viewsets.ModelViewSet):
    queryset = TempInto.objects.all()
    serializer_class = TempIntoSerializer


class TempintoFileViewSet(viewsets.ModelViewSet):
    serializer_class = TempintoFileSerializer

    def get_queryset(self):
        return TempintoFile.objects.filter(tempinto_id=self.kwargs['tempinto_pk'])

    def get_serializer_context(self):
        return {'tempinto_id': self.kwargs['tempinto_pk']}
