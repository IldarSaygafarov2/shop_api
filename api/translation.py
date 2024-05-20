from modeltranslation.translator import TranslationOptions, translator

from . import models


class CollectionTranslationOptions(TranslationOptions):
    fields = ["title"]


class ProductTranslationOptions(TranslationOptions):
    fields = ["title", "description", "compound"]


translator.register(models.Collection, CollectionTranslationOptions)
translator.register(models.Product, ProductTranslationOptions)
