# Generated by Django 4.2 on 2023-11-18 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('day', models.DateField(default=datetime.date.today)),
                ('item', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='recyclestats',
            name='paper',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
