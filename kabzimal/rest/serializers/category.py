from rest_framework import serializers

from kabzimal.models import CategoryModel
from kabzimal.rest.serializers.category_type import CategoryTypeSerializers


class CategorySerializers(serializers.ModelSerializer):
    category_type = CategoryTypeSerializers()

    class Meta:
       model = CategoryModel
       fields = ('category_name','category_desc','category_picture','is_active','category_type',)