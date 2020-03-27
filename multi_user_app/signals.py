from django.dispatch import receiver
from django.contrib.auth import user_logged_in,user_logged_out
from .models import loged_in_detail


@receiver(user_logged_in)
def Loged_user(sender,**kwargs):
    data=loged_in_detail.objects.get_or_create(user=kwargs.get('user'))


@receiver(user_logged_out)
def Loged_out_user(sender,**kwargs):

    logout=loged_in_detail.objects.get(user=kwargs.get('user')).delete()


