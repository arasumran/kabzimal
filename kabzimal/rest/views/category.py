# -*- coding: utf-8 -*-
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from kabzimal.models import CategoryModel
from kabzimal.rest.serializers.category import CategorySerializers


class CategoryViewSet(ModelViewSet):
    search_fields = '__all__'
    ordering_fields = '__all__'
    serializer_class = CategorySerializers
    queryset = CategoryModel.objects.all()