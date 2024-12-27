from rest_framework.response import Response
from rest_framework import views, status

from customers import serializers
from customers import models


class TenantSignUpTemplateView(views.APIView):

    def post(self, request, format=None):
        serializer = serializers.TemplateSerializer(
            data=request.data, context={"tenant": request.tenant}
        )
        if serializer.is_valid():
            serializer.save(tenant=request.tenant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
