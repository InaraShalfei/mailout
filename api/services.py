import time

from django.utils import timezone

from api.models import Client, Message


def process_planned_message(pk):
    message = Message.objects.get(id=pk)
    if message.mailout.finish_time < timezone.now():
        message.status = 'is_cancelled'
        message.save()
        return
    send_message = SendMessage()
    send_message.send_message(message.client.phone_number, message.mailout.text)
    message.status = 'is_sent'
    message.save()


class SendMessage:
    def send_message(self, phone_number, text):
        print(f'Message "{text}" for {phone_number}')
        # TODO use external API for sending messages


class MailoutService:
    def process(self, mailout):
        clients = self.get_clients(mailout)
        for client in clients:
            message = Message.objects.create(client=client, status='is_planned',
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
