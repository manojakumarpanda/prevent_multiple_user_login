from django.contrib import admin
from .models import loged_in_detail
# Register your models here.


class login_detail(admin.ModelAdmin):
    list_display = ['user','id']

admin.site.register(loged_in_detail,login_detail)