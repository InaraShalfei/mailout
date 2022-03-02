import json
import os
from dotenv import load_dotenv
import requests
from django.utils import timezone

from api.models import Client, Message

load_dotenv()


def process_planned_message(pk):
    message = Message.objects.get(id=pk)
    if message.mailout.finish_time < timezone.now():
        message.status = 'is_cancelled'
        message.save()
        return
    send_message = SendMessage()
    successful = send_message.send_message(message)
    if successful:
        message.status = 'is_sent'
    else:
        message.status = 'error'
    message.save()


class SendMessage:
    def send_message(self, message):
        try:
            data = {
                'id': message.id,
                'phone': int(message.client.phone_number),
                'text': message.mailout.text
            }
            response = requests.post(
                f'https://probe.fbrq.cloud/v1/send/{message.id}',
                data=json.dumps(data),
                headers={'Authorization': f'Bearer {os.getenv("TOKEN")}'})
            if response.json().get('message') != 'OK':
                return False
            return True
        except:
            return False


class MailoutService:
    def process(self, mailout):
        clients = self.get_clients(mailout)
        for client in clients:
            message = Message.objects.create(client=client,
                                             status='is_planned',
                                             mailout=mailout)
            process_planned_message(message.id)

    def get_clients(self, mailout):
        operator_code = mailout.filter.get('operator_code')
        tag = mailout.filter.get('tag')
        clients = Client.objects
        if operator_code:
            clients = clients.filter(operator_code=operator_code)
        if tag:
            clients = clients.filter(tag=tag)

        return clients.all()
