from django.shortcuts import render
from rest_framework import viewsets, mixins
# Create your views here.
from rest_framework.decorators import action

from invoiceapp.models import Invoice, InvoiceItem
from invoiceapp.serializers import InvoiceSerializer, InvoiceItemReadSerializer, \
    InvoiceItemWriteSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    This viewset can do CRUD for Invoices.
    """
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()


class InvoiceItemViewSet(viewsets.ModelViewSet):
    """
    This Viewset can do CRUD for InvoiceItems of certain Invocie.
    """

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InvoiceItemReadSerializer
        return InvoiceItemWriteSerializer

    def get_queryset(self):
        return InvoiceItem.objects.filter(invoice=self.kwargs['invoice_pk'])

    def create(self, request, *args, **kwargs):
        request.data['invoice'] = kwargs['invoice_pk']
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data['invoice'] = kwargs['invoice_pk']
        return super().update(request, *args, **kwargs)


class GlobalInvoiceItemViewSet(viewsets.ModelViewSet):
    """
    This viewset can do CRUD for InvoiceItems directly.
    It means that it can handle the any InvoiceItems of any Invoice.
    """
    queryset = InvoiceItem.objects.select_related("invoice")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InvoiceItemReadSerializer
        return InvoiceItemWriteSerializer
