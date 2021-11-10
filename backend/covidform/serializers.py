from .models import TempInto, TempintoFile
from rest_framework import serializers


class TempIntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempInto
        fields = '__all__'


class TempintoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempintoFile
        fields = '__all__'
