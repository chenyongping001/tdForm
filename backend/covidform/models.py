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
        choices=HEALTH_CHOICE, default=0)
    daysValue = models.PositiveSmallIntegerField(
        choices=DAYS_CHOICE, default=0)
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
    tempinto = models.ForeignKey(TempInto, on_delete=models.CASCADE)
