from rest_framework import viewsets

from api.models import Client, MailOut
from api.serializers import ClientSerializer, MailOutSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailOutViewSet(viewsets.ModelViewSet):
    queryset = MailOut.objects.all()
    serializer_class = MailOutSerializer
