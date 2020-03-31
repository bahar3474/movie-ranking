from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('login/check', views.check_login, name='check_login')
]