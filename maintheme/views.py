from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Post
from django.utils import timezone


from .models import Post

def maintheme_list(request):
    return render(request, 'maintheme/index.html', {})
def contacts(request):
    return render(request, 'maintheme/contacts.html', {})
def post(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'maintheme/news.html', {'posts': posts})
