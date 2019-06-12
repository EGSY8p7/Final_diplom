from django.db import models

class Title(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    time = models.DateTimeField(null=True, blank=True)
    aqi = models.IntegerField()

