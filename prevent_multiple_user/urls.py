"""prevent_multiple_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from multi_user_app import views
from django.contrib.auth import views as User_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/',User_view.LoginView.as_view(template_name='multi_user_app/login.html'),name='login'),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.logout_user,name='logout'),
    #path('logout/',User_view.LogoutView.as_view(),name='logout'),
    path('user/',views.Create_user.as_view(),name='create'),
    path('',views.Create_user.as_view(),name='home'),
    path('accounts/profile/',views.Home_view.as_view(),name='home'),

]
