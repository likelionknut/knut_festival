# Generated by Django 2.2.5 on 2019-09-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190918_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='board/images/%Y/%m/%d/%H/%M'),
        ),
        migrations.AlterField(
            model_name='boothpromotionboard',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='boothPromotionBoard/images/%Y/%m/%d/%H/%M'),
        ),
        migrations.AlterField(
            model_name='freeboard',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='free/images/%Y/%m/%d/%H/%M'),
        ),
        migrations.AlterField(
            model_name='freeboard',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='free/videos/%Y/%m/%d/%H/%M'),
        ),
        migrations.AlterField(
            model_name='friendsboard',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='friends/images/%Y/%m/%d/%H/%M'),
        ),
    ]
