from django.urls import path
from .views import check_login, register, login

urlpatterns = [
    path('login', login, name='login'),
    path('login/check', check_login, name='check_login'),
    path('register', register, name='register')
]
