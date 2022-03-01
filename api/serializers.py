from rest_framework import serializers

from api.models import Client, MailOut, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'operator_code', 'tag', 'timezone')

    def to_internal_value(self, data):
        data['operator_code'] = data['phone_number'][1:4]

        return super(ClientSerializer, self).to_internal_value(data)


class MailOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailOut
        fields = ('id', 'start_time', 'finish_time', 'text', 'filter')


class MessageSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    class Meta:
        model = Message
        fields = ('creation_time', 'status', 'client')
