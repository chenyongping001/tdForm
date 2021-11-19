from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from datetime import datetime, timedelta
from .models import TempInto, TempintoFile
from .serializers import TempIntoSerializer, TempintoFileSerializer


class TempIntoViewSet(viewsets.ModelViewSet):
    queryset = TempInto.objects.all()
    serializer_class = TempIntoSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        weixinID = self.request.query_params.get('weixinid')
        queryset = TempInto.objects.all()
        if(status):
            queryset = queryset.filter(status=status)
        if(days and days.isnumeric()):
            end_date = datetime.today()
            start_date = end_date - timedelta(days=int(days))
            queryset = queryset.filter(
                createtime__range=[start_date, end_date])
        if(weixinID):
            queryset = queryset.filter(weixinID=weixinID)
        return queryset.order_by("-createtime")


class TempintoFileViewSet(viewsets.ModelViewSet):
    serializer_class = TempintoFileSerializer

    def get_queryset(self):
        return TempintoFile.objects.filter(tempinto_id=self.kwargs['tempinto_pk'])

    def get_serializer_context(self):
        return {'tempinto_id': self.kwargs['tempinto_pk']}
