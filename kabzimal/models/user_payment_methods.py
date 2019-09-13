from django.contrib.auth.models import User

from kabzimal.models.user import UserModel
from kabzimal.models.payments import PaymentsModels

__author__ = 'umran'
from django.db import models


class UserPaymentsMethods(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,db_column='user_id')
    credit_card_number = models.CharField(max_length=500,db_column='credit_number')
    payment_method_details = models.TextField(db_column='details')
    payments_method_code = models.IntegerField(db_column='payment_method_code')

    class Meta:
        db_table = 'kabzimal_user_payment_method'

