# Generated by Django 4.2 on 2023-11-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_rename_day_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recyclestats',
            name='compost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='daily_streak',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='glass',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='metal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='plastic',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='trash',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='xp',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
