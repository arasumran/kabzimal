from rest_framework import serializers

from kabzimal.models import ProductsModel, CategoryModel
from kabzimal.rest.serializers.category import CategorySerializers


class ProductsSerializers(serializers.ModelSerializer):
    product_category = CategorySerializers()

    class Meta:
        model = ProductsModel
        fields = ('product_name', 'product_price', 'product_size', 'product_count',
                  'product_description','product_category',)
