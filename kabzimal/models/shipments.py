from kabzimal.models.invocies import InvoicesModels
from kabzimal.models.order import OrdersModel
from kabzimal.utils.mixins import TimeStampMixin

__author__ = 'umran'
from django.db import models


class ShipmentModels(TimeStampMixin):
    order = models.ForeignKey(OrdersModel, models.CASCADE,db_column='order_id')
    invoices_number = models.ForeignKey(InvoicesModels,on_delete=models.CASCADE,db_column='invoices_id')
    shipment_tracking_number = models.IntegerField(db_column='shipment_tracking_number')
    shipment_date = models.DateField(db_column='shipment_date')
    shipment_details= models.CharField(db_column='shipment_details',max_length=500)

    class Meta:
        db_table = 'kabzimal_shipment'

