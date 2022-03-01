from rest_framework import serializers

from api.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'operator_code', 'tag', 'timezone')

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number')
        operator_code = phone_number[0:4]
        client = Client.objects.create(operator_code=operator_code,
                                       **validated_data)
        return client
