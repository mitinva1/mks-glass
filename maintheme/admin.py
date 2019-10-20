from django.contrib import admin
from .models import Photo, Post

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text',
             'created_date', 
              'img',
              'published_date',]
admin.site.register(Post, PostAdmin)
admin.site.register(Photo)
# admin.site.register()

# Register your models here.







