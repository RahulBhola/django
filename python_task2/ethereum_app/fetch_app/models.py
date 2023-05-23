from django.db import models

# Create your models here.
class EthereumTransaction(models.Model):
    address = models.CharField(max_length=42)
    balance = models.DecimalField(max_digits=20, decimal_places=4)
    timestamp = models.DateTimeField()