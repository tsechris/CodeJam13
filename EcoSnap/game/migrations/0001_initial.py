# Generated by Django 4.2 on 2023-11-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecycleStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('xp', models.IntegerField()),
                ('plastic', models.IntegerField()),
                ('glass', models.IntegerField()),
                ('metal', models.IntegerField()),
                ('trash', models.IntegerField()),
                ('compost', models.IntegerField()),
                ('daily_streak', models.IntegerField()),
                ('has_recycled_today', models.BooleanField(default=False)),
            ],
        ),
    ]
