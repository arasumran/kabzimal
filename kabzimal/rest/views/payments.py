# -*- coding: utf-8 -*-


from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from kabzimal.models import OrdersModel, PaymentsModels
from kabzimal.rest.serializers.orders import OrdersSerializers
from kabzimal.rest.serializers.payments import PaymentsSerializers


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentsSerializers
    queryset = PaymentsModels.objects.all()
