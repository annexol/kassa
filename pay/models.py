from django.db import models


# Create your models here.


class UserName(models.Model):
    name = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
