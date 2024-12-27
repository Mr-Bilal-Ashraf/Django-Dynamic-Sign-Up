from rest_framework import serializers

from customers import models


class FieldSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    type = serializers.CharField(required=True)
    required = serializers.BooleanField(required=True)
    max_length = serializers.IntegerField(required=False)
    max_digits = serializers.IntegerField(required=False)
    decimal_places = serializers.IntegerField(required=False)

    def validate(self, attrs):
        field_type = attrs.get("type")

        if field_type == "char":
            if "max_length" not in attrs:
                raise serializers.ValidationError(
                    "'max_length' is required for 'char' type."
                )
            max_length = attrs.get("max_length")
            if max_length is None or max_length >= 255:
                raise serializers.ValidationError(
                    "'max_length' must not be null OR greater than 255."
                )

        elif field_type == "decimal":
            if "max_digits" not in attrs or "decimal_places" not in attrs:
                raise serializers.ValidationError(
                    "'max_digits' and 'decimal_places' are required for 'decimal' type."
                )
            if attrs.get("max_digits") is None or attrs.get("decimal_places") is None:
                raise serializers.ValidationError(
                    "'max_digits' and 'decimal_places' must not be null."
                )

        return attrs


class StepSerializer(serializers.Serializer):
    step = serializers.IntegerField(required=True)
    fields = FieldSerializer(many=True)


class TemplateSerializer(serializers.Serializer):
    steps = StepSerializer(many=True)

    def validate(self, data):
        tenant = self.context.get("tenant")
        if models.TenantSignUpTemplate.objects.filter(tenant=tenant).exists():
            raise serializers.ValidationError(
                {"detail": "Template already exists, try updating"}
            )
        return data

    def save(self, **kwargs):
        obj = models.TenantSignUpTemplate.objects.create(
            tenant=kwargs.get("tenant"), fields=self.validated_data
        )
        return obj
