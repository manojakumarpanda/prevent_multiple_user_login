from django.contrib.sessions.models import Session
from .models import loged_in_detail
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_protect


class Login_session_middleware():
    def __init__(self,get_response):
        self.get_response=get_response


    def __call__(self,request,*args, **kwargs):

        if request.user.is_authenticated:
            current_session_key=request.user.user_session.sesson_key
            if current_session_key and current_session_key!=request.session.session_key:
                print(current_session_key,request.session.session_key)
                Session.objects.get(session_key=current_session_key).delete()

            request.user.user_session.sesson_key=request.session.session_key
            request.user.user_session.save()

        response=self.get_response(request)
        return response

