# Generated by Django 2.2.5 on 2019-09-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_comment_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=10)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]