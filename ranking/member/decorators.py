from django.shortcuts import render


def member_only(view_func):
    def wrap(request, *args, **kwargs):
        if 'member_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, "member/login.html", {'login_required': True})
    return wrap