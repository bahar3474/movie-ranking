from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from .models import Member
from .decorators import member_only


def login(request):
    return render(request, 'member/login.html', {})


def check_login(request):
    try:
        member_login = Member.objects.get(
            username=request.POST['user'],
            password=make_password(request.POST['pass'], Member.salt)
        )
        request.session['member_id'] = member_login.id
        return HttpResponseRedirect('/')

    except Member.DoesNotExist:
        return render(request, 'member/login.html', {'not_found': True})
