from django.core import mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers, filters
from constance import config
from django.conf import settings


@api_view(['GET'])
def home_page_settings(request):
    consts = dir(config)
    languages = [lang[0] for lang in settings.LANGUAGES]

    res = {}
    for lang in languages:
        res[lang] = {}
        for const in consts:
            if const.lower().endswith(lang):
                res[lang][const.lower()] = getattr(config, const)
        if lang == 'ru':
            for const in consts:
                if const in ['GENERAL_ADDRESS', 'GENERAL_WORKING_TIME']:
                    res['ru'][const.lower()] = getattr(config, const)
    return Response(res)


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
