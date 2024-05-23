from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


@admin.register(models.Collection)
class CollectionAdmin(TranslationAdmin):
    fields = ["title"]


class ProductGalleryInline(admin.TabularInline):
    model = models.ProductGallery
    extra = 1


@admin.register(models.Product)
class ProductAdmin(TranslationAdmin):
    fields = ["title", "description", "compound", "image", "collection", 'main_type']
    inlines = [ProductGalleryInline]


admin.site.register(models.Certificates)
