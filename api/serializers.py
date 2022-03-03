import pytz as pytz
from django.utils import timezone

from rest_framework import serializers

from api.models import Client, MailOut, Message
from mailout.tasks import process_delayed_mailout


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

    def create(self, validated_data):
        mailout = super().create(validated_data)
        if (mailout.start_time.astimezone(pytz.utc) < timezone.now()
                < mailout.finish_time.astimezone(pytz.utc)):
            process_delayed_mailout.delay(mailout.id)
        elif mailout.start_time.astimezone(pytz.utc) > timezone.now():
            process_delayed_mailout.apply_async(
                args=[mailout.id],
                eta=mailout.start_time.astimezone(pytz.utc))
        return mailout


class MessageSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Message
        fields = ('creation_time', 'status', 'client')
