# Generated by Django 3.2 on 2022-07-26 10:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20220724_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffsubmission',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
