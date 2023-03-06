from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Nanna(requset):
    return HttpResponse("I miss you nanna")

def Amma(request):
    return HttpResponse("I love u")