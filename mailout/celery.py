from celery import Celery

app = Celery('mailout',
             broker='amqp://localhost',
             include=['mailout.tasks'])

if __name__ == '__main__':
    app.start()
