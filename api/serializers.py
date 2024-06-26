from rest_framework import serializers

from . import models


class HomeImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeImages
        fields = ['mobile_image', 'desktop_image']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = ['image']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = ["pk", "title"]


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductGallery
        fields = ["image"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductGallerySerializer(many=True, read_only=True)
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
            "weight",
            "food_value",
            "energy_value",
            "date",
        ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certificates
        fields = ['pk', 'image']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = ['pk', 'title', 'description', 'year', 'company_name']