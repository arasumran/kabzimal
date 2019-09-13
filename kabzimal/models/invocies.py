from kabzimal.models.order import OrdersModel

__author__ = 'umran'
from django.db import models


class InvoicesModels(models.Model):
    invoices_status_code = models.CharField(db_column='invocies_status_code',max_length=250)
    order = models.ForeignKey(OrdersModel,on_delete=models.CASCADE,db_column='order_id')
    invoices_date = models.DateField(db_column='inocies_date')
    invoice_details= models.CharField(db_column='invoices_details',max_length=500)

    class Meta:

        db_table = 'kabzimal_invoices'

