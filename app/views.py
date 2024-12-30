from rest_framework import generics, viewsets

from customers.serializers import TemplateSerializer
from customers import models as CustomerModels


class SignUpTemplateView(generics.ListAPIView):
    queryset = CustomerModels.SignUpTemplate.objects.all()
    serializer_class = TemplateSerializer
