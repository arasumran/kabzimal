# -*- coding: utf-8 -*-


from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from kabzimal.models import OrdersModel
from kabzimal.rest.serializers.orders import OrdersSerializers


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializers
    queryset = OrdersModel.objects.all()
