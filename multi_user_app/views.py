from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views.generic import View
from .forms import User_form,Login_form
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .middleware import *
from django.middleware import csrf


# Create your views here.
class Create_user(View):
    form_class = User_form
    template_name = 'multi_user_app/form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context={'form':form,'title': 'User_add form'}
        return render(request, self.template_name, context=context)


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            print(form.data)
            username=form.cleaned_data.get('username')
            password=form.cleaned_data['password']
            user=User(username=username,email=form.cleaned_data['email'])
            user.set_password(raw_password=password)
            user.save()
            return HttpResponseRedirect('accounts/profile/')
        context = self.context={'form':form,'title': 'User_add form'}
        return render(request, self.template_name, context=context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def LoginView(request):
    form=Login_form()
    if request.method=='POST':
        form=Login_form(request.POST or None)
        if form.is_valid():
            print(csrf.get_token(request))
            uname=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                mobile=int(uname)
                global username
                user=User.objects.filter(user_extra__mobile=mobile)
                username=user[0].username
            except ValueError:
                    if '@' in uname:
                        user = User.objects.filter(user_extra__email=uname)
                        username=user[0].username
                    else :
                        username=uname

            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print(request.session.session_key)

                return render(request,'multi_user_app/home.html',{'title':'home_page'})
            else:
                return messages.ERROR(request,'Invalid credentional')
    return render(request,'multi_user_app/login.html',{'form':form})


class Home_view(View):
    template_name='multi_user_app/home.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'title':'home_page'})