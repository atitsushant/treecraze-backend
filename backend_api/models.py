from django.db import models

class GarbageReport(models.Model):
    photo = models.ImageField(upload_to='reports/')
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    submitted_at = models.DateTimeField(auto_now_add=True)