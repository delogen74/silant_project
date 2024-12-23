from django.db import models
from machines.models import Machine

class Reclamation(models.Model):
    failure_date = models.DateField(blank=True, null=True)
    operating_time = models.PositiveIntegerField(default=0)
    failure_node = models.CharField(max_length=200, blank=True, null=True)
    failure_description = models.TextField(blank=True, null=True)
    recovery_method = models.CharField(max_length=200, blank=True, null=True)
    used_parts = models.TextField(blank=True, null=True)
    recovery_date = models.DateField(blank=True, null=True)
    downtime = models.PositiveIntegerField(default=0)
    service_company = models.CharField(max_length=200, blank=True, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='claims')

    def __str__(self):
        return f"{self.failure_node} [{self.failure_date}]"
