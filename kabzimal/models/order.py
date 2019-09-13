from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from kabzimal.models.user import UserModel

__author__ = 'umran'
from kabzimal.utils.mixins import TimeStampMixin
from django.db import models

class OrdersModel(TimeStampMixin):
    STATUS_TAKEN = '1'
    STATUS_RESERVED = '3'
    STATUS_PLANNED = '2'
    STATUS_SHIPPED='4'
    STATUS_DELETED = '6'
    STATUS_ARRIVED = '5'
    STATUS_DEFAULT = '0'
    STATUS_EXPIRED = '7'

    STATUS = ((STATUS_TAKEN, _('Taken')),
              (STATUS_EXPIRED, _('Expired')),
              (STATUS_PLANNED, _('Planned')),
              (STATUS_RESERVED, _('Reserved')),
              (STATUS_SHIPPED, _('Shipped')),
              (STATUS_ARRIVED, _('Ariived')),
              (STATUS_DELETED, _('Deleted')),

    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='user_id')
    order_status_code = models.CharField(_('Status'),max_length=2,choices=STATUS,default=STATUS_DEFAULT,db_column='order_status_code',unique=True)
    date_order_placed= models.CharField(_('Date Order Placed'), max_length=300,db_column='date_order_placed')
    order_details = models.CharField(_('Order Details'),max_length=500,db_column='order_detail')

    class Meta:
        db_table = 'kabzimal_orders'


