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

    def create(self, validated_data):
        tempinto_id = self.context['tempinto_id']
        return TempintoFile.objects.create(tempinto_id=tempinto_id, **validated_data)
