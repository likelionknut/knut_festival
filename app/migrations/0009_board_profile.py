# Generated by Django 2.2.5 on 2019-09-17 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_board_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='profile',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
