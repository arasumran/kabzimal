from rest_framework import serializers

from kabzimal.models import  CategoryTypeModel, ProductsModel, OrderItemsModel
from kabzimal.rest.serializers.orders import OrdersSerializers
from kabzimal.rest.serializers.prodcuts import ProductsSerializers


class OrderItemsSerializers(serializers.ModelSerializer):
    product = ProductsSerializers()
    order = OrdersSerializers()
    class Meta:
        model = OrderItemsModel
        fields = ('order_item_quantity','order_item_price','order_number','order_item_price', 'order_issued_by','order','product',)


class OrderItemsAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItemsModel
        fields = '__all__'