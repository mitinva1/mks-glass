# Generated by Django 2.2.5 on 2019-10-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintheme', '0002_article_choice_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
