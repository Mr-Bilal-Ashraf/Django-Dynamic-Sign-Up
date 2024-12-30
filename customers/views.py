from rest_framework.decorators import action
from rest_framework import viewsets

from customers import serializers
from customers import models
from rest_framework import status
from rest_framework.response import Response


class SignUpTemplateView(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.TemplateSerializer
    queryset = models.SignUpTemplate.objects.all()


class TenantViewSet(viewsets.ModelViewSet):
    """
    All tenant related APIs should be here, like create tenant in the server, update its config etc
    """
    # serializer_class = serializers.TenantSerializer
    queryset = models.Tenant.objects.all()

    @action(detail=True, methods=["patch"])
    def update_tenant_template(self, request, pk=None, template_id=None):
        tenant = self.get_object()
        template = models.SignUpTemplate.objects.filter(pk=template_id).last()
        if not template:
            return Response(
                {"detail": "SignUp template not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        tenant.signup_template = template
        tenant.save()
        return Response(status=status.HTTP_200_OK)
