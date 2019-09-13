from datetime import datetime

import django

__author__ = 'umran'

from django.db import models
from kabzimal.utils.mixins import TimeStampMixin
from kabzimal.models.products import ProductsModel
from kabzimal.models.order import OrdersModel
class OrderItemsModel(TimeStampMixin):
    product = models.ForeignKey(ProductsModel, models.CASCADE,db_column='product_id')
    order = models.ForeignKey(OrdersModel,on_delete=models.CASCADE,db_column='order_id')
    order_item_status_code = models.ForeignKey(OrdersModel,on_delete= models.DO_NOTHING, to_field='order_status_code',related_name='order_item_status_code', db_column='order_status_code_id')
    order_item_quantity = models.CharField(max_length=500,db_column='order_item_quantity')
    order_item_price = models.FloatField(db_column='order_item_price')
    order_number = models.IntegerField(db_column='order_number')
    order_issued_by = models.CharField(max_length=500,db_column='order_issued_by')
    order_issued_date = models.DateField(default=django.utils.timezone.now,db_column='order_issued_date')

    class Meta:
        db_table = 'kabzimal_order_items'





