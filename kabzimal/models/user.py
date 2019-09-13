from django.contrib.auth.models import User,AbstractUser

__author__ = 'umran'


from django.db import models


class UserModel(AbstractUser):
    FEMALE = 'F'
    MALE = 'M'
    NOT_GIVEN = 'X'
    GENDER = [
        (FEMALE, 'Felame'),
        (MALE, 'Male'),
        (NOT_GIVEN, 'Unknown'),
            ]
    address_line = models.CharField(max_length=500,db_column='adress_line_1')
    address_line = models.CharField(max_length=500,db_column='address_line_2')
    town_city = models.CharField(db_column='town',max_length=255)
    country = models.CharField(max_length=255,db_column='country')
    gender = models.CharField(db_column='gender',choices=GENDER,default=NOT_GIVEN,max_length=10)
    phone_number = models.CharField(db_column='phone_number',max_length=11)


    class Meta:
        db_table = 'auth_user'

