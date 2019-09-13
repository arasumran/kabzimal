from kabzimal.models.invocies import InvoicesModels

__author__ = 'umran'

from django.db import models


class PaymentsModels(models.Model):
    invoice_number = models.ForeignKey(InvoicesModels,on_delete=models.CASCADE,db_column='invoice_number_id')
    payment_date = models.DateTimeField(db_column='payment_date')
    payment_amount = models.FloatField(db_column='payment_amount')

    class Meta:
        db_table = 'kabzimal_payments'

