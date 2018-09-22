from django.db import models

# Create your models here.
from django.db import models


class UserTb(models.Model):
    user = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tb'

class login():
    def signup():
        b = UserTb(user='userr', password='pass')
        b.save()
