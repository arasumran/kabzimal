from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from kabzimal.rest.views.category import CategoryViewSet
from kabzimal.rest.views.category_type import CategoryTypeViewSet
from kabzimal.rest.views.invoices import InvoicesViewSet
from kabzimal.rest.views.orders import OrdersViewSet
from kabzimal.rest.views.oreder_items import OrderItemsViewSet
from kabzimal.rest.views.payments import PaymentsViewSet
from kabzimal.rest.views.products import ProductsViewSet
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()

router.register('category', CategoryViewSet, basename="category")
router.register('category-type', CategoryTypeViewSet, basename="category-type")
router.register('products', ProductsViewSet, basename="products")
router.register('orders', OrdersViewSet, basename="orders")
router.register('order-items', OrderItemsViewSet, basename="order-items")
router.register('payments', PaymentsViewSet, basename="payments")
router.register('invoices', InvoicesViewSet, basename="invoices")
router.register('invoices', InvoicesViewSet, basename="invoices")



urlpatterns = [
    url(r'^', include(router.urls)),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
