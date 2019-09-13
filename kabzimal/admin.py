from django.contrib import admin

# Register your models here.
from django.contrib import admin
from kabzimal.models.category_type import CategoryTypeModel
from kabzimal.models.category import CategoryModel
admin.site.register(CategoryTypeModel)
admin.site.register(CategoryModel)