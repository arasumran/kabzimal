# Generated by Django 2.2.5 on 2019-09-11 12:17

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('address_line', models.CharField(db_column='address_line_2', max_length=500)),
                ('town_city', models.CharField(db_column='town', max_length=255)),
                ('country', models.CharField(db_column='country', max_length=255)),
                ('gender', models.CharField(choices=[('F', 'Felame'), ('M', 'Male'), ('X', 'Unknown')], db_column='gender', default='X', max_length=10)),
                ('phone_number', models.CharField(db_column='phone_number', max_length=11)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('category_name', models.CharField(db_column='category_type', max_length=255)),
                ('category_desc', models.CharField(db_column='category_desc', max_length=255)),
                ('category_picture', models.CharField(db_column='category_pitcure', max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'kabzimal_category',
            },
        ),
        migrations.CreateModel(
            name='CategoryTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('category_type_name', models.CharField(db_column='category_type_name', max_length=255)),
                ('category_type_desc', models.TextField(db_column='c_type_desc')),
            ],
            options={
                'verbose_name': 'CategoryType',
                'verbose_name_plural': 'CategoryTypes',
                'db_table': 'kabzimal_category_type',
            },
        ),
        migrations.CreateModel(
            name='InvoicesModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoices_status_code', models.CharField(db_column='invocies_status_code', max_length=250)),
                ('invoices_date', models.DateField(db_column='inocies_date')),
                ('invoice_details', models.CharField(db_column='invoices_details', max_length=500)),
            ],
            options={
                'db_table': 'kabzimal_invoices',
            },
        ),
        migrations.CreateModel(
            name='OrdersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_status_code', models.CharField(choices=[('1', 'Taken'), ('7', 'Expired'), ('2', 'Planned'), ('3', 'Reserved'), ('4', 'Shipped'), ('5', 'Ariived'), ('6', 'Deleted')], db_column='order_status_code', default='0', max_length=2, unique=True, verbose_name='Status')),
                ('date_order_placed', models.CharField(db_column='date_order_placed', max_length=300, verbose_name='Date Order Placed')),
                ('order_details', models.CharField(db_column='order_detail', max_length=500, verbose_name='Order Details')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kabzimal_orders',
            },
        ),
        migrations.CreateModel(
            name='UserPaymentsMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_number', models.CharField(db_column='credit_number', max_length=500)),
                ('payment_method_details', models.TextField(db_column='details')),
                ('payments_method_code', models.IntegerField(db_column='payment_method_code')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kabzimal_user_payment_method',
            },
        ),
        migrations.CreateModel(
            name='ShipmentModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shipment_tracking_number', models.IntegerField(db_column='shipment_tracking_number')),
                ('shipment_date', models.DateField(db_column='shipment_date')),
                ('shipment_details', models.CharField(db_column='shipment_details', max_length=500)),
                ('invoices_number', models.ForeignKey(db_column='invoices_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.InvoicesModels')),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.OrdersModel')),
            ],
            options={
                'db_table': 'kabzimal_shipment',
            },
        ),
        migrations.CreateModel(
            name='ShipmentItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.OrdersModel')),
                ('shipment', models.ForeignKey(db_column='shipment_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.ShipmentModels')),
            ],
            options={
                'db_table': 'kabzimal_shipment_items',
            },
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(db_column='p_name', max_length=500)),
                ('product_price', models.FloatField(db_column='p_price')),
                ('product_size', models.IntegerField(db_column='p_size')),
                ('product_count', models.BigIntegerField(db_column='p_count')),
                ('product_description', models.TextField(db_column='p_description', null=True)),
                ('product_category', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.CategoryModel')),
            ],
            options={
                'db_table': 'kabzimal_products',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(db_column='payment_date')),
                ('payment_amount', models.FloatField(db_column='payment_amount')),
                ('invoice_number', models.ForeignKey(db_column='invoice_number_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.InvoicesModels')),
            ],
            options={
                'db_table': 'kabzimal_payments',
            },
        ),
        migrations.CreateModel(
            name='OrderItemsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_item_quantity', models.CharField(db_column='order_item_quantity', max_length=500)),
                ('order_item_price', models.FloatField(db_column='order_item_price')),
                ('order_number', models.IntegerField(db_column='order_number')),
                ('order_issued_by', models.CharField(db_column='order_issued_by', max_length=500)),
                ('order_issued_date', models.DateField(db_column='order_issued_date', default=django.utils.timezone.now)),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.OrdersModel')),
                ('order_item_status_code', models.ForeignKey(db_column='order_status_code_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_item_status_code', to='kabzimal.OrdersModel', to_field='order_status_code')),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.ProductsModel')),
            ],
            options={
                'db_table': 'kabzimal_order_items',
            },
        ),
        migrations.AddField(
            model_name='invoicesmodels',
            name='order',
            field=models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.OrdersModel'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='category_type_id',
            field=models.ForeignKey(db_column='category_type_id', on_delete=django.db.models.deletion.CASCADE, to='kabzimal.CategoryTypeModel'),
        ),
    ]
