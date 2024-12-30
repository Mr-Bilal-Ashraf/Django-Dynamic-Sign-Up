from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customers.serializers import TemplateSerializer
from customers import models as CustomerModels


@api_view(['GET'])
def my_signup_template(request):
    if request.tenant.signup_template:
        return Response(request.tenant.signup_template.fields)
    return Response("No template found")
