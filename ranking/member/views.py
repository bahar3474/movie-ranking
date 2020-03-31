from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Member


def login(request):
    return render(request, 'member/login.html', {})


def check_login(request):
    try:
        member_login = Member.objects.get(
            username=request.POST['user'],
            password=make_password(request.POST['pass'], Member.salt)
        )
        request.session['member_id'] = member_login.id

    except Member.DoesNotExist:
        return render(request, 'member/login.html', {'not_found': True})
