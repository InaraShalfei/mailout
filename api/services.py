from api.models import Client

class SendMessage:
    def send_message(self, phone_number, text):
        print(f'Message "{text}" for {phone_number}')
        # TODO use external API for sending messages


class MailoutService:
    def process(self, mailout):
        send_message = SendMessage()
        clients = self.get_clients(mailout)
        for client in clients:
            send_message.send_message(client.phone_number, mailout.text)

    def get_clients(self, mailout):
        return Client.objects.filter(
            operator_code=mailout.filter.get('operator_code'),
            tag=mailout.filter.get('tag'))
