from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers, filters
from django.core import mail


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ProductFilter


@api_view(['POST'])
def send_mail(request):
    print(request.data)
    msg = f"""
Имя: {request.data['name']}
Номер телефона: {request.data['phone']}
Почта: {request.data['email']}    
    """
    mail.send_mail(
        subject='Обратная связь с сайта',
        message=msg,
        from_email='sayildar17@gmail.com',
        recipient_list=['sayildar17@gmail.com']
    )
    return Response({'message': "Данные отправлены"})

# temp = {
#     "name": "Ildar",
#     "phone": "+998900000000",
#     "email": "sayildar17@gmail.com"
# }
