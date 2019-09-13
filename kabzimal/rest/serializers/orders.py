from rest_framework import serializers

from kabzimal.models import  CategoryTypeModel, ProductsModel, OrdersModel


class OrdersSerializers(serializers.ModelSerializer):
   class Meta:
       model = OrdersModel
       fields = '__all__'