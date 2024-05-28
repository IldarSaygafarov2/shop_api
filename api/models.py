from django.db import models


class Collection(models.Model):
    title = models.CharField(verbose_name="Название", max_length=155)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    class MainTypeChoices(models.TextChoices):
        DOBROE = ("dobroe", 'Доброе')
        ALSAFI = ("alsafi", 'Альсафи')

    title = models.CharField(verbose_name="Название", max_length=155)
    description = models.TextField(verbose_name="Описание", default='Описание')
    compound = models.TextField(verbose_name="Состав", default='Состав')
    image = models.ImageField(verbose_name="Фото", upload_to="products/images/", null=True, blank=True)
    collection = models.ForeignKey(
        verbose_name="Категория", to=Collection, on_delete=models.CASCADE,
        default='', null=True, blank=True
    )
    main_type = models.CharField(max_length=10, choices=MainTypeChoices, default=MainTypeChoices.DOBROE)
    is_new = models.BooleanField(default=False, verbose_name='Новинка ?', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", null=True, blank=True
    )
    image = models.ImageField(verbose_name="Фото", upload_to="products/images/")

    def __str__(self) -> str:
        return f"Фото: {self.product.title}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"


class Certificates(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='certificates/images/')

    def __str__(self):
        return f'Сертификат №{self.pk}'

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class HomeImages(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='homepage/images/')

    class Meta:
        verbose_name = 'Фото на слайдере'
        verbose_name_plural = 'Фотки на слайдере'


class Partner(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='partners/images/')

    class Meta:
        verbose_name = 'Фото партнера'
        verbose_name_plural = 'Фото партнеров'