from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from django.db.models import Count

from api.models import Client, MailOut
from api.serializers import (ClientSerializer, MailOutSerializer,
                             MessageSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailOutViewSet(viewsets.ModelViewSet):
    queryset = MailOut.objects.all()
    serializer_class = MailOutSerializer

    @action(detail=True, url_path='messages')
    def get_messages(self, request, pk):
        mailout = MailOut.objects.get(id=pk)
        messages = mailout.messages.all()
        serializer = ListSerializer(child=MessageSerializer(),
                                    context=self.get_serializer_context())
        return Response(serializer.to_representation(messages),
                        status=status.HTTP_200_OK)

    @action(detail=True, url_path='statistics')
    def get_statistics(self, request, pk):
        mailout = MailOut.objects.get(id=pk)
        result = mailout.messages.all().values('status').annotate(
            count=Count('mailout')).order_by()
        return Response(result, status=status.HTTP_200_OK)
