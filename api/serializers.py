from rest_framework import serializers

from . import models


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = ["pk", "title"]


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductGallery
        fields = ["image"]


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    collection = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Product
        fields = [
            "pk",
            "title",
            "description",
            "compound",
            "image",
            "images",
            "collection",
            # "main_type",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = [
            models.ProductGallery.objects.get(pk=pk).image.url for pk in data["images"]
        ]
        data["images"] = images
        return data


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certificates
        fields = ['pk', 'image']


