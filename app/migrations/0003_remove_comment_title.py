# Generated by Django 2.2.5 on 2019-09-14 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
