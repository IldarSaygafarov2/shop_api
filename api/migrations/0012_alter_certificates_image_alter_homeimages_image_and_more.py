# Generated by Django 5.0.6 on 2024-06-03 16:21

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_certificates_image_alter_homeimages_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='certificates/images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='homeimages',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='homepage/images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='partners/images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='products/images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=0.5, size=[1920, 1080], upload_to='products/images/', verbose_name='Фото'),
        ),
    ]
