# Generated by Django 3.2.3 on 2021-06-17 16:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ArticleNation', '0003_article_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
