from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
