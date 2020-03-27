from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class loged_in_detail(models.Model):
    user       =models.OneToOneField(User,related_name='user_session',on_delete=models.CASCADE)
    mob_number =models.BigIntegerField(null=True,blank=True)
    sesson_key =models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table='logedin_data'

class User_extra(models.Model):
    user    =models.OneToOneField(User,related_name='user_extra',on_delete=models.CASCADE)
    mobile  =models.BigIntegerField(blank=True)
    email   =models.EmailField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.user.username





