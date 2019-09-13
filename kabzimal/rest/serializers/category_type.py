from rest_framework import serializers

from kabzimal.models import  CategoryTypeModel


class CategoryTypeSerializers(serializers.ModelSerializer):
   class Meta:
       model = CategoryTypeModel
       fields = ('category_type_name','category_type_desc',)