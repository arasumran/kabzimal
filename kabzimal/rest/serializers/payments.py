from rest_framework import serializers

from kabzimal.models import PaymentsModels


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentsModels
        fields = '__all__'
