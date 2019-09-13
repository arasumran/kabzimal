# -*- coding: utf-8 -*-


from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from kabzimal.models import CategoryTypeModel
from kabzimal.rest.serializers.category_type import CategoryTypeSerializers


class CategoryTypeViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryTypeSerializers
    queryset = CategoryTypeModel.objects.all()
