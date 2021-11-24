from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
import json
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from .models import TempInto, TempintoFile
from .serializers import TempIntoSerializer, TempintoFileSerializer


class TempIntoViewSet(viewsets.ModelViewSet):
    serializer_class = TempIntoSerializer

    def get_queryset(self):
        queryset = TempInto.objects.all()
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        weixinID = self.request.query_params.get('weixinid')
        if(status and status.isnumeric()):
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


class QJTempinto(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        queryset = TempInto.objects.all().order_by("-createtime")
        if(id and id.isnumeric()):
            queryset = queryset.filter(id=id)
        if(status and status.isnumeric()):
            queryset = queryset.filter(status=status)
        if(days and days.isnumeric()):
            end_date = datetime.today()
            start_date = end_date - timedelta(days=int(days))
            queryset = queryset.filter(
                createtime__range=[start_date, end_date])

        serializer = TempIntoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(self.request.body.decode('utf-8'))
        id = data.get("id")
        status = data.get("status")
        if(id and status):
            try:
                TempInto.objects.filter(id=id).update(status=status)
                return JsonResponse(model_to_dict(TempInto.objects.get(id=id)))
            except:
                pass
        return JsonResponse({"status": "error"})
