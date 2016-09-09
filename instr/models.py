from django.db import models

class Subdivision(models.Model):
    title = models.CharField(max_length=100)

class Leading(models.Model):
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FilePathField()
