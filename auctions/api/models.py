from django.db import models

# Create your models here.
class UserInfo(models.Model):
    phone = models.CharField(verbose_name="手机",max_length=11,unique=True)
