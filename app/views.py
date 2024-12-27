from django.http import HttpResponse
from django.shortcuts import render

from django_tenants.utils import get_tenant_model


def abc(request):
    t = get_tenant_model().objects.get(schema_name=request.tenant.schema_name)
    return HttpResponse(f"Hello {t.name}")
