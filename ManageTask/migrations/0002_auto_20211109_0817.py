# Generated by Django 3.2.9 on 2021-11-09 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 8, 17, 24, 492676)),
        ),
    ]