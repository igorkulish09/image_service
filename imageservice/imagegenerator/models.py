from django.db import models


class GeneratedImage(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=7)
    title = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    image_url = models.URLField()
