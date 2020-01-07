#my changes all
from django.contrib.sites.models import Site#my
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор')
    title = models.CharField(max_length=200, verbose_name='название поста')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='дата убликации')
    img = models.ImageField(upload_to='media/img/', 
                       verbose_name='Грузи епт', null = True, blank = True)
                       

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Photo(models.Model):
    photo_text = models.CharField(max_length=35, verbose_name='название')
    pub_date = models.DateTimeField('Дата публикации')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='Загрузка фото', null = True, blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='photo_posts', verbose_name='автор')
    def __str__(self):
        return self.photo_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class PhotoFrameless(models.Model):
    PhotoFrameless_text = models.CharField(max_length=35, verbose_name='название')
    pub_date = models.DateTimeField('Дата публикации')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='Загрузка фото', null = True, blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='frameless_posts', verbose_name='автор')
    def __str__(self):
        return self.PhotoFrameless_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Gate(models.Model):
    gate_text = models.CharField(max_length=35, verbose_name='название')
    pub_date = models.DateTimeField('Дата публикации')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='Загрузка фото', null = True, blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='blog_posts', verbose_name='автор')
    def __str__(self):
        return self.gate_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Pvc(models.Model):
    Pvc_text = models.CharField(max_length=35, verbose_name='название')
    pub_date = models.DateTimeField('Дата публикации')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='Загрузка фото', null = True, blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='pvc_posts', verbose_name='автор')
    def __str__(self):
        return self.Pvc_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Metall(models.Model):
    metall_text = models.CharField(max_length=35, verbose_name='название')
    pub_date = models.DateTimeField('Дата публикации')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='Загрузка фото', null = True, blank = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='metall_posts', verbose_name='автор')
    def __str__(self):
        return self.metall_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Photo1(models.Model):
#     photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
#     photo1_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.photo1_text

class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    about = models.CharField(max_length=200)


#for news
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title