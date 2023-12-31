# Generated by Django 4.2.5 on 2023-11-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=200)),
                ('class_date', models.DateTimeField(verbose_name='date published')),
                ('points', models.DateTimeField(max_length=20)),
            ],
        ),
    ]
