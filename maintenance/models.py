from django.db import models
from machines.models import Machine

class TO(models.Model):
    to_type = models.CharField(max_length=100)
    date_performed = models.DateField(blank=True, null=True)
    operating_time = models.PositiveIntegerField(default=0)
    order_number = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    service_company = models.CharField(max_length=200, blank=True, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='to_records')

    def __str__(self):
        return f"{self.to_type} (№{self.order_number})"


class Maintenance(models.Model):
    machine = models.ForeignKey('machines.Machine', on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Maintenance for {self.machine} on {self.date}"