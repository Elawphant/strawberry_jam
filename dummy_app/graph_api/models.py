from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=10, blank=False, default="Peach")
    ripen = models.BooleanField(default=False)
