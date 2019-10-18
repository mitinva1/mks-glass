from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Раздел в стадии разработки")
# Create your views here.
