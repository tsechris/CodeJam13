# Generated by Django 4.2 on 2023-11-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recyclestats',
            name='compost',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='daily_streak',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='glass',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='metal',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='plastic',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='trash',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recyclestats',
            name='xp',
            field=models.PositiveIntegerField(),
        ),
    ]