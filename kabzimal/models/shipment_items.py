from kabzimal.models.order import OrdersModel
from kabzimal.models.shipments import ShipmentModels

__author__ = 'umran'
from django.db import models


class ShipmentItems(models.Model):
    shipment = models.ForeignKey(ShipmentModels, on_delete=models.CASCADE, db_column='shipment_id')
    order = models.ForeignKey(OrdersModel, on_delete=models.CASCADE, db_column='order_id')

    class Meta:
        db_table = 'kabzimal_shipment_items'


