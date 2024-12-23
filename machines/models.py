from django.db import models

class Machine(models.Model):
    factory_number = models.CharField(max_length=100, unique=True)
    machine_model = models.CharField(max_length=100, blank=True, null=True)
    engine_model = models.CharField(max_length=100, blank=True, null=True)
    engine_number = models.CharField(max_length=100, blank=True, null=True)
    transmission_model = models.CharField(max_length=100, blank=True, null=True)
    transmission_number = models.CharField(max_length=100, blank=True, null=True)
    drive_axle_model = models.CharField(max_length=100, blank=True, null=True)
    drive_axle_number = models.CharField(max_length=100, blank=True, null=True)
    steerable_axle_model = models.CharField(max_length=100, blank=True, null=True)
    steerable_axle_number = models.CharField(max_length=100, blank=True, null=True)

    shipment_date = models.DateField(blank=True, null=True)
    consignee = models.CharField(max_length=200, blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=200, blank=True, null=True)
    service_company = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Машина №{self.factory_number}"
