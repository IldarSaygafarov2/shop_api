from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers, models


# @api_view(["GET"])
# def root(request):
#     return Response("server is running")


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer