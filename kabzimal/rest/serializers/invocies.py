from rest_framework import serializers

from kabzimal.models import InvoicesModels


class InvociesSerializers(serializers.ModelSerializer):
    class Meta:
        model = InvoicesModels
        fields = '__all__'
