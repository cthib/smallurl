from django.db import models

from .base_62_converter import dehydrate
from smallurl.settings import BASE_URL


class Url(models.Model):
    long = models.CharField(max_length=200)
    short = models.CharField(max_length=20)

    def __str__(self):
        return self.long

    def set_short(self):
        self.short = "{}{}".format(BASE_URL, dehydrate(self.id))
        self.save()