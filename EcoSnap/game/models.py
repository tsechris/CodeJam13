from django.db import models
from datetime import date

# Create your models here.
class RecycleStats(models.Model):
    user = models.CharField(max_length=100)
    xp = models.PositiveIntegerField(default=0)
    plastic = models.PositiveIntegerField(default=0)
    glass = models.PositiveIntegerField(default=0)
    metal = models.PositiveIntegerField(default=0)
    paper = models.PositiveIntegerField(default = 0)
    trash = models.PositiveIntegerField(default=0)
    compost = models.PositiveIntegerField(default=0)
    daily_streak = models.PositiveIntegerField(default=0)
    has_recycled_today = models.BooleanField(default=False)

class History(models.Model):
    user = models.CharField(max_length=100)
    day = models.DateField(default=date.today)
    item = models.CharField(max_length=50)