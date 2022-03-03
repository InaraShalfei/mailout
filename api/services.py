from api.models import Client, Message, MailOut
from mailout.send_message import process_planned_message


class MailoutService:
    def process(self, mailout):
        clients = self.get_clients(mailout)
        for client in clients:
            message = Message.objects.create(client=client,
                                             status='is_planned',
                                             mailout=mailout)
            process_planned_message(message)

    def get_clients(self, mailout):
        operator_code = mailout.filter.get('operator_code')
        tag = mailout.filter.get('tag')
        clients = Client.objects
        if operator_code:
            clients = clients.filter(operator_code=operator_code)
        if tag:
            clients = clients.filter(tag=tag)

        return clients.all()


def process_planned_mailout(pk):
    mailout = MailOut.objects.get(id=pk)
    mailout_service = MailoutService()
    mailout_service.process(mailout)
