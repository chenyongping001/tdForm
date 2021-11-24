from typing import Any
from django.conf import settings
from django.db import models
from rest_framework.response import Response

# Create your models here.


class TempInto(models.Model):
    HEALTH_CHOICE = [
        (1, '绿码'),
        (0, '非绿码')
    ]
    DAYS_CHOICE = [
        (1, '1天'),
        (2, '2天'),
        (3, '3天'),
    ]
    OUT_PROVINCE_CHOICE = [
        (0, '未出过省'),
        (1, '出过省'),
    ]
    STATUS_CHOICE = [
        (0, '待处理'),
        (1, '找不到对应联系人'),
        (2, '已生成申请单'),
        (3, '审批中'),
        (4, '通过'),
        (5, '拒绝'),
        (6, '已删除'),
    ]

    weixinID = models.CharField(max_length=255)
    name = models.CharField(max_length=10)
    iccard = models.CharField(max_length=18)
    healthValue = models.PositiveSmallIntegerField(
        choices=HEALTH_CHOICE, default=1)
    daysValue = models.PositiveSmallIntegerField(
        choices=DAYS_CHOICE, default=1)
    outProvinceValue = models.PositiveSmallIntegerField(
        choices=OUT_PROVINCE_CHOICE, default=0)
    outCompany = models.CharField(max_length=255)
    project = models.CharField(max_length=255, null=True, blank=True)
    reason = models.TextField()
    note = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=10)
    contactPhone = models.CharField(max_length=11)
    createtime = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICE, default=0)


class TempintoFile(models.Model):
    file = models.ImageField(upload_to='covid19/')
    tempinto = models.ForeignKey(
        TempInto, related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return settings.MEDIA_URL+str(self.file)
