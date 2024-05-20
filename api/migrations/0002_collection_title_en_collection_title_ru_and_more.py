# Generated by Django 5.0.6 on 2024-05-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='collection',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='collection',
            name='title_uz',
            field=models.CharField(max_length=155, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='compound_en',
            field=models.TextField(null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='product',
            name='compound_ru',
            field=models.TextField(null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='product',
            name='compound_uz',
            field=models.TextField(null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=155, null=True, verbose_name='Название'),
        ),
    ]
