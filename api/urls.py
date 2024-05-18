from django.urls import path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('collections', views.CollectionViewSet)
router.register('products', views.ProductViewSet)


urlpatterns = []
urlpatterns += router.urls
