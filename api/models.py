from django.db import models


class Collection(models.Model):
    title = models.CharField(verbose_name='Название', max_length=155)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=155)
    description = models.TextField(verbose_name='Описание')
    compound = models.TextField(verbose_name='Состав')
    image = models.ImageField(verbose_name='Фото', upload_to='products/images/')
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=6)
    collection = models.ForeignKey(verbose_name='Категория', to=Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
