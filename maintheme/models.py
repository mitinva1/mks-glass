#my changes all
from django.contrib.sites.models import Site#my
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(upload_to='media/img/', 
                       verbose_name='Грузи епт', null = True, blank = True)
                       

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Photo(models.Model):
    photo_text = models.CharField(max_length=35)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='грузи картинку', null = True, blank = True)
    def __str__(self):
        return self.photo_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class PhotoFrameless(models.Model):
    PhotoFrameless_text = models.CharField(max_length=35)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='грузи картинку', null = True, blank = True)
    def __str__(self):
        return self.PhotoFrameless_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Gate(models.Model):
    gate_text = models.CharField(max_length=35)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='грузи картинку', null = True, blank = True)
    def __str__(self):
        return self.gate_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Pvc(models.Model):
    Pvc_text = models.CharField(max_length=35)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='грузи картинку', null = True, blank = True)
    def __str__(self):
        return self.Pvc_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Metall(models.Model):
    metall_text = models.CharField(max_length=35)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='media/img/gallery/',
                       verbose_name='грузи картинку', null = True, blank = True)
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