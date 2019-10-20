from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'maintheme'
urlpatterns = [
    path('', views.maintheme_list, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.post, name='news'),
              ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)