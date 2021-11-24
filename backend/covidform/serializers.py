from .models import TempInto, TempintoFile
from rest_framework import serializers


class TempintoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempintoFile
        fields = ['file']

    def create(self, validated_data):
        tempinto_id = self.context['tempinto_id']
        return TempintoFile.objects.create(tempinto_id=tempinto_id, **validated_data)


class TempIntoSerializer(serializers.ModelSerializer):
    files = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TempInto
        fields = ["id",
                  "weixinID",
                  "name",
                  "iccard",
                  "healthValue",
                  "daysValue",
                  "outProvinceValue",
                  "outCompany",
                  "project",
                  "reason",
                  "note",
                  "contact",
                  "contactPhone",
                  "createtime",
                  "last_update",
                  "status",
                  "files"]
