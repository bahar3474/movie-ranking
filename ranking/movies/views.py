from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def top5(request):
    return HttpResponse('hello! :)')
