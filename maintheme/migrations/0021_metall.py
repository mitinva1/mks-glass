# Generated by Django 2.2.5 on 2019-10-28 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintheme', '0020_pvc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metall_text', models.CharField(max_length=35)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/img/gallery/', verbose_name='грузи картинку')),
            ],
        ),
    ]
