from django.urls import path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('collections', views.CollectionViewSet)
router.register('certificates', views.CertificateViewSet)
router.register('products/dobroe', views.ProductViewSet, basename='dobroe-products')
router.register('products/alsafi', views.ProductAlsafiViewSet, basename='alsafi-products')
router.register('products/newest', views.NewProductsViewSet, basename='newest-products')


urlpatterns = [
    path('send_mail/', views.send_mail),
    path('vars/', views.home_page_settings),
    path('images/', views.get_products_images)
]
urlpatterns += router.urls
