import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('RABBITMQ_USERNAME')
password = os.getenv('RABBITMQ_PASSWORD')
app = Celery('mailout',
             broker=f'amqp://{user}:{password}@rabbitmq',
             include=['mailout.tasks'])

if __name__ == '__main__':
    app.start()
