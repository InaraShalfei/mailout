import json
import os

import pytz as pytz
from dotenv import load_dotenv
import requests
from django.utils import timezone


load_dotenv()


def process_planned_message(message):
    if message.mailout.finish_time.astimezone(pytz.utc) < timezone.now():
        message.status = 'is_cancelled'
        message.save()
        return
    successful = send_message(message)
    if successful:
        message.status = 'is_sent'
    else:
        message.status = 'error'
    message.save()


def send_message(message):
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
        return response.json().get('message') == 'OK'
    except Exception as e:
        print(e.args)
        return False
