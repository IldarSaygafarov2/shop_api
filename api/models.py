from django.db import models
from django_resized import ResizedImageField


class Collection(models.Model):
    title = models.CharField(verbose_name="Название", max_length=155)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    class MainTypeChoices(models.TextChoices):
        DOBROE = ("dobroe", "Доброе")
        ALSAFI = ("alsafi", "Альсафи")

    title = models.CharField(verbose_name="Название", max_length=155)
    description = models.TextField(verbose_name="Описание", default="Описание")
    compound = models.TextField(verbose_name="Состав", default="Состав")
    image = ResizedImageField(
        verbose_name="Фото", upload_to="products/images/", null=True, blank=True, force_format='WEBP'
    )
    weight = models.CharField(max_length=150, verbose_name='Объем', null=True, blank=True)
    food_value = models.CharField(max_length=150, verbose_name='Пищевая ценность', null=True, blank=True)
    energy_value = models.CharField(max_length=150, verbose_name='Энергетическая ценность', null=True, blank=True)
    date = models.CharField(max_length=150, verbose_name='Срок годности', null=True, blank=True)
    collection = models.ForeignKey(
        verbose_name="Категория",
        to=Collection,
        on_delete=models.CASCADE,
        default="",
        null=True,
        blank=True,
    )
    main_type = models.CharField(
        max_length=10, choices=MainTypeChoices, default=MainTypeChoices.DOBROE
    )
    is_new = models.BooleanField(
        default=False, verbose_name="Новинка ?", null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", null=True, blank=True
    )
    image = ResizedImageField(verbose_name="Фото", upload_to="products/images/", force_format='WEBP')

    def __str__(self) -> str:
        return f"Фото: {self.product.title}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"


class Certificates(models.Model):
    image = ResizedImageField(verbose_name="Фото", upload_to="certificates/images/", force_format='WEBP')

    def __str__(self):
        return f"Сертификат №{self.pk}"

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"


class HomeImages(models.Model):
    mobile_image = models.ImageField(verbose_name="Фото на телефоны",
                                     upload_to="homepage/images/",
                                     null=True, blank=True)
    desktop_image = models.ImageField(verbose_name="Фото на десктоп",
                                      upload_to="homepage/images/",
                                      null=True, blank=True)

    class Meta:
        verbose_name = "Фото на слайдере"
        verbose_name_plural = "Фотки на слайдере"


class Partner(models.Model):
    image = ResizedImageField(verbose_name="Фото", upload_to="partners/images/", force_format='WEBP')

    class Meta:
        verbose_name = "Фото партнера"
        verbose_name_plural = "Фото партнеров"


class About(models.Model):
    year = models.CharField(max_length=30, verbose_name='Года')
    company_name = models.CharField(max_length=40, verbose_name='Название компании', default='BIO NATURAL FOOD')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент истории'
        verbose_name_plural = 'Элементы истории'