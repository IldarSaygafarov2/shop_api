from rest_framework import serializers

from . import models


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = ['pk', 'title']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ['pk', 'title', 'description', 'compound', 'image', 'collection']