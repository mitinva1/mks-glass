from django.contrib import admin
from .models import Photo, Post, PhotoFrameless, Gate, Pvc, Metall

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text',
             'created_date', 
              'img',
              'published_date',]
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(PhotoFrameless)
admin.site.register(Gate)
admin.site.register(Pvc)
admin.site.register(Metall)
# admin.site.register()

# Register your models here.







