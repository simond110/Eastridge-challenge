from django.urls import path, include
from rest_framework_nested import routers
from invoiceapp.views import InvoiceViewSet, InvoiceItemViewSet, GlobalInvoiceItemViewSet

r = routers.DefaultRouter()
r.register(r'invoices', InvoiceViewSet)
r.register(r'invoice-items', GlobalInvoiceItemViewSet, basename="global-invoice-items")
invoice_items_router = routers.NestedDefaultRouter(r, r'invoices', lookup="invoice")
invoice_items_router.register(r'items', InvoiceItemViewSet, basename="invoice-items")

app_name = "invoiceapp"

urlpatterns = [
    path('', include(r.urls)),
    path('', include(invoice_items_router.urls))
]
