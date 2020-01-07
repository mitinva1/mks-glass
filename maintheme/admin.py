from django.contrib import admin
from .models import Photo, Post, PhotoFrameless, Gate, Pvc, Metall

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text',
             'created_date', 
              'img',
              'published_date',]
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date', 'author')
    list_filter = ('created_date', 'published_date', 'author')
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_text', 'pub_date', 'author')
    list_filter = ('pub_date', 'author')
@admin.register(PhotoFrameless)
class FramelessAdmin(admin.ModelAdmin):
    list_display = ('PhotoFrameless_text', 'pub_date', 'author')
    list_filter = ('pub_date', 'author')
@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ('gate_text', 'pub_date', 'author')
    list_filter = ('pub_date', 'author')
    search_fields = ('gate_text', 'pub_date')
@admin.register(Pvc)
class PvcAdmin(admin.ModelAdmin):
    list_display = ('Pvc_text', 'pub_date', 'author')
    list_filter = ('pub_date', 'author')
@admin.register(Metall)
class MetallAdmin(admin.ModelAdmin):
    list_display = ('metall_text', 'pub_date', 'author')
    list_filter = ('pub_date', 'author')
# admin.site.register()

# Register your models here.







