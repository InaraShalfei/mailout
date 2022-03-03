from api.services import process_planned_mailout
from .celery import app


@app.task
def process_delayed_mailout(pk):
    process_planned_mailout(pk)
