from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from kabzimal.utils.mixins import *
from kabzimal.models.category_type import CategoryTypeModel


class CategoryModel(AuditMixin):
    category_type = models.ForeignKey(CategoryTypeModel,on_delete=models.CASCADE, db_column='category_type_id')
    category_name = models.CharField(db_column='category_type',max_length=255)
    category_desc = models.CharField(db_column='category_desc',max_length=255)
    category_picture = models.ImageField(upload_to='static//images/',db_column='category_pitcure')
    is_active = models.BooleanField(default=False)



    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        db_table = 'kabzimal_category'

    def __unicode__(self):
        return self.category_name

    def __str__(self):
        return self.category_name



