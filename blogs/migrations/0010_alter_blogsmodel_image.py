# Generated by Django 4.1.7 on 2023-04-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_blogsmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsmodel',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='blog_images/'),
        ),
    ]
