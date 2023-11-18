from django.db import models

# Create your models here.
class Log(models.Model):
    level =  models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    resourceId = models.CharField(max_length=50)
    timestamp =  models.DateTimeField()
    traceId =  models.CharField(max_length=70)
    spanId = models.CharField(max_length=50)
    commit = models.CharField(max_length=50)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.traceId
    
