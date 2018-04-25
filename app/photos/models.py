from django.db import models


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)
