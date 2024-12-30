from rest_framework import generics, viewsets, mixins

from customers.serializers import TemplateSerializer
from customers import models as CustomerModels


class SignUpTemplateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    queryset = CustomerModels.SignUpTemplate.objects.all()
    serializer_class = TemplateSerializer

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
