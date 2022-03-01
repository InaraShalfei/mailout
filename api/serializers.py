from rest_framework import serializers

from api.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'operator_code', 'tag', 'timezone')

    def to_internal_value(self, data):
        data['operator_code'] = data['phone_number'][1:4]

        return super(ClientSerializer, self).to_internal_value(data)
