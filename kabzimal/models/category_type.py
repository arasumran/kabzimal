from django.utils.translation import ugettext_lazy as _

from kabzimal.utils.mixins import *


class CategoryTypeModel(AuditMixin):
    category_type_name = models.CharField(max_length=255, db_column='category_type_name')
    category_type_desc = models.TextField(db_column='c_type_desc')

    class Meta:
        verbose_name = _('CategoryType')
        verbose_name_plural = _('CategoryTypes')
        db_table = 'kabzimal_category_type'

    def __str__(self):
        return self.category_type_name
    def __unicode__(self):
        return self.category_type_name
