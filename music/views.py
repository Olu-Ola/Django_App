from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1> This is my Music App Homepage </H1>")
# Create your views here.
