from django.urls import path

from . import views

app_name = 'maintheme'
urlpatterns = [
    path('', views.post_list, name='index'),
              ]