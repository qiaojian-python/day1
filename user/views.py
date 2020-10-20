from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    print('this is first view')

    return HttpResponse("ok")


def user_login(request):
    print('this is dev view')
    return HttpResponse('y')