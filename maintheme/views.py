from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic



def maintheme_list(request):
    return render(request, 'maintheme/index.html', {})
def contacts(request):
    return render(request, 'maintheme/contacts.html', {})
