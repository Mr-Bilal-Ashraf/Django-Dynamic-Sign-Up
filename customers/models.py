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


class SignUpTemplate(models.Model):
    fields = models.JSONField()


# fields expected data in following format
#
# [
#     {"step": 1, "fields": [{"name": "username", "type": "char", "required": True, "max_length": 50}]},
#     {"step": 2, "fields": [{"name": "email", "type": "email", "required": True}]},
#     {"step": 3, "fields": [{"name": "age", "type": "integer", "required": False}]}
# ]
