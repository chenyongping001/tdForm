from django.db import models

# Create your models here.


class TempInto(models.Model):
    HEALTH_CHOICE = [
        (0, '绿码'),
        (1, '非绿码')
    ]
    DAYS_CHOICE = [
        (0, '1天'),
        (1, '2天'),
        (2, '3天'),
    ]
    OUT_PROVINCE_CHOICE = [
        (0, '未出过省'),
        (1, '出过省'),
    ]

    weixinID = models.CharField(max_length=255)
    name = models.CharField(max_length=10)
    iccard = models.CharField(max_length=18)
    healthValue = models.PositiveSmallIntegerField(
        choices=HEALTH_CHOICE, default=0)
    daysValue = models.PositiveSmallIntegerField(
        choices=DAYS_CHOICE, default=0)
    outProvinceValue = models.PositiveSmallIntegerField(
        choices=OUT_PROVINCE_CHOICE, default=0)
    outCompany = models.CharField(max_length=255)
    project = models.CharField(max_length=255, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=10)
    contactPhone = models.CharField(max_length=11)
    createtime = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default="待处理")


class TempintoFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='covid19/')
    tempinto = models.ForeignKey(TempInto, on_delete=models.CASCADE)
