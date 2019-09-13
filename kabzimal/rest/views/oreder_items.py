from kabzimal.rest.serializers.order_items import OrderItemsSerializers, OrderItemsAddSerializers

# -*- coding: utf-8 -*-


from rest_framework import viewsets

from kabzimal.models import OrderItemsModel


class OrderItemsViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action in ['POST']:
            return OrderItemsAddSerializers
        else:
            return OrderItemsSerializers
    def get_queryset(self):
        return OrderItemsModel.objects.all()
