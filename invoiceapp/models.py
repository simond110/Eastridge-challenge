from django.db import models


# Create your models here.
class Invoice(models.Model):
    date = models.DateField()


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="invoice_items")
    units = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField()