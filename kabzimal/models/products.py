__author__ = 'umran'
from django.db import models

from kabzimal.utils.mixins import TimeStampMixin
from kabzimal.models.category import CategoryModel

class ProductsModel(TimeStampMixin):
    product_category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,db_column='category_id')
    product_name = models.CharField(max_length=500, db_column='p_name', null=False)
    product_price = models.FloatField(db_column='p_price', null=False)
    product_size  = models.IntegerField(db_column='p_size')
    product_count = models.BigIntegerField(db_column='p_count')
    product_description = models.TextField(db_column='p_description',null=True)

    class Meta:
        db_table = 'kabzimal_products'

