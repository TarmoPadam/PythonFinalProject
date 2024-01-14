from django.db import models


# Create your models here.


class Variables(models.Model):
    website_title = models.CharField(max_length=20, null=True, blank=True)
