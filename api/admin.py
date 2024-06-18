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

    list_display = ["title", "description", "compound", "image", "weight", "food_value", "energy_value", "date",
                    "collection", 'main_type', 'is_new']
    fieldsets = [
        (
            "Общее",
            {
                'fields': ["title", "description", "compound", "image", "collection", 'main_type', 'is_new']
            }
        ),
        (
            "Характеристики",
            {
               'fields': ["weight", "food_value", "energy_value", "date"]
            }
        )
    ]
    inlines = [ProductGalleryInline]


@admin.register(models.About)
class AboutAdmin(TranslationAdmin):
    fields = ['title', 'description', 'year', 'company_name']


admin.site.register(models.Certificates)
admin.site.register(models.HomeImages)
admin.site.register(models.Partner)
