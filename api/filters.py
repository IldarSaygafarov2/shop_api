from django_filters import FilterSet, AllValuesFilter
from api import models


class ProductFilter(FilterSet):
    collection = AllValuesFilter(field_name="collection__title")

    class Meta:
        model = models.Product
        fields = ["collection"]
