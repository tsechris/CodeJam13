from django.db import models

# Create your models here.
class RecycleStats(models.Model):
    user = models.CharField(max_length=100)
    xp = models.PositiveIntegerField()
    plastic = models.PositiveIntegerField()
    glass = models.PositiveIntegerField()
    metal = models.PositiveIntegerField()
    trash = models.PositiveIntegerField()
    compost = models.PositiveIntegerField()
    daily_streak = models.PositiveIntegerField()
    has_recycled_today = models.BooleanField(default=False)