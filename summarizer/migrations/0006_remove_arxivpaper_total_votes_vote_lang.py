# Generated by Django 4.1.6 on 2023-02-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0005_remove_arxivpaper_blog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arxivpaper',
            name='total_votes',
        ),
        migrations.AddField(
            model_name='vote',
            name='lang',
            field=models.CharField(default='en', max_length=10),
        ),
    ]