# -*- coding: utf-8 -*-


from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from kabzimal.models import ProductsModel
from kabzimal.rest.serializers.prodcuts import ProductsSerializers


class ProductsViewSet(viewsets.ModelViewSet):
    search_fields = '__all__'
    ordering_fields = '__all__'
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return ProductsModel.objects.all()
    def get_serializer_class(self):
        return ProductsSerializers


