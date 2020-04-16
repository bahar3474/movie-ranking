from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from .models import Member
from .decorators import member_only
from .forms import RegisterForm


def login(request):
    return render(request, 'member/login.html', {})


def check_login(request):
    try:
        member_login = Member.objects.get(
            username=request.POST.get('user'),
            password=make_password(request.POST.get('pass'), Member.salt)
        )
        request.session['member_id'] = member_login.id
        return HttpResponseRedirect('/')

    except Member.DoesNotExist:
        return render(request, 'member/login.html', {'not_found': True})

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, "member/register.html", context)

