from django.db import models
from datetime import date

# Create your models here.
class RecycleStats(models.Model):
    user = models.CharField(max_length=100)
    xp = models.PositiveIntegerField()
    plastic = models.PositiveIntegerField()
    glass = models.PositiveIntegerField()
    metal = models.PositiveIntegerField()
    paper = models.PositiveIntegerField(default = 0)
    trash = models.PositiveIntegerField()
    compost = models.PositiveIntegerField()
    daily_streak = models.PositiveIntegerField()
    has_recycled_today = models.BooleanField(default=False)

class History(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    item = models.CharField(max_length=50)
