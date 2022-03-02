from .celery import app
from mailout.send_message import process_planned_message


@app.task
def send_delayed_message(pk):
    process_planned_message(pk)
