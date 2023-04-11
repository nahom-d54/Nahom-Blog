
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .globals import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lambda request: redirect('home'),name='index'),
    path('blog/',include('blog.urls'),name='posts'),
    path('accounts/login/',views.login,name='sign_in'),
    path('accounts/sign_up/',views.sign_up,name='sign_up')
]
