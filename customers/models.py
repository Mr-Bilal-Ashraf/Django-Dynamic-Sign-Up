from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass


class TenantSignUpTemplate(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE)
    fields = models.JSONField()
