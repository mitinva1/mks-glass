# Generated by Django 2.2.5 on 2019-10-18 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintheme', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='question_text',
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='photo1',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintheme.Photo'),
        ),
    ]
