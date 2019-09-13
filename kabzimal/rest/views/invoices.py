# -*- coding: utf-8 -*-


from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from kabzimal.models import InvoicesModels
from kabzimal.rest.serializers.invocies import InvociesSerializers


class InvoicesViewSet(viewsets.ModelViewSet):
    serializer_class = InvociesSerializers
    queryset = InvoicesModels.objects.all()
