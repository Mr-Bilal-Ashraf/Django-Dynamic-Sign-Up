from rest_framework import viewsets

from customers import serializers
from customers import models


class SignUpTemplateView(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = serializers.TemplateSerializer
    queryset = models.SignUpTemplate.objects.all()
