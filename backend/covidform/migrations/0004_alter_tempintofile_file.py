# Generated by Django 3.2.9 on 2021-12-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidform', '0003_auto_20211123_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempintofile',
            name='file',
            field=models.FileField(upload_to='covid19/'),
        ),
    ]
