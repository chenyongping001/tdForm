# Generated by Django 3.2.9 on 2021-12-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidform', '0006_overtimeinto_gatevalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtimeinto',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '待处理'), (1, '无此持卡人'), (2, '找不到联系人'), (3, '已生成申请单'), (4, '审批中'), (5, '通过'), (6, '已删除'), (7, '施工证已过期')], default=0),
        ),
    ]
