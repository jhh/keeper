from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Activity(models.Model):
    name = models.CharField(max_length=200)
    meta = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class Action(models.Model):
    activity = models.ForeignKey(
        Activity, related_name="actions", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    measures = ArrayField(models.CharField(max_length=20))
    meta = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class Trace(models.Model):
    action = models.ForeignKey(Action, related_name="traces", on_delete=models.CASCADE)
    milliseconds = models.PositiveIntegerField()
    measurements = ArrayField(models.FloatField())
