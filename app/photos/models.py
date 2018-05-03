from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)


@receiver(pre_delete, sender=Photo)
def file_delete(sender, instance, **kwargs):
    instance.file.delete()
