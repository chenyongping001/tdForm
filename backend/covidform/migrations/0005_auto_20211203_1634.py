# Generated by Django 3.2.9 on 2021-12-03 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidform', '0004_alter_tempintofile_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='OvertimeInto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weixinID', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=10)),
                ('iccard', models.CharField(max_length=18)),
                ('reason', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(max_length=10)),
                ('contactPhone', models.CharField(max_length=11)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '待处理'), (1, '无此持卡人'), (2, '找不到联系人'), (3, '已生成申请单'), (4, '审批中'), (5, '通过'), (6, '已删除')], default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='tempinto',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '待处理'), (1, '找不到联系人'), (2, '已生成申请单'), (3, '审批中'), (4, '通过'), (5, '拒绝'), (6, '已删除')], default=0),
        ),
        migrations.CreateModel(
            name='OvertimeIntoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='covid19_OT/')),
                ('overtimeinto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='covidform.overtimeinto')),
            ],
        ),
    ]
