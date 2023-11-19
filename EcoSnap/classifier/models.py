from django.db import models


class Classifier(models.Model):
    classification = models.CharField(max_length=200)
    class_date =  models.DateTimeField("date published")
    points = models.DateTimeField(max_length = 20)

