# Generated by Django 2.2.5 on 2019-09-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_board_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='tag',
            field=models.CharField(choices=[('found', '주웠어요'), ('lost', '잃어버렸어요')], max_length=2),
        ),
    ]
