# Generated by Django 2.2.5 on 2019-10-20 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintheme', '0008_person_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Photo1',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]