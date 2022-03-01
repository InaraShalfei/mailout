import pytz as pytz
from django.db import models
from django.core.validators import RegexValidator

from api.validators import JSONSchemaValidator

MAILOUT_FILTER_FIELD_SCHEMA = {
    'type': 'object',
    'properties': {
        'tag': {'type': 'string'},
        'operator_code': {'type': 'string'}
    }
}


class MailOut(models.Model):
    start_time = models.DateTimeField(verbose_name='время запуска рассылки')
    finish_time = models.DateTimeField(verbose_name='время окончания рассылки')
    text = models.TextField(verbose_name='текст сообщения')
    filter = models.JSONField(default=dict, validators=[JSONSchemaValidator(
        limit_value=MAILOUT_FILTER_FIELD_SCHEMA)],
                              verbose_name='фильтр свойств рассылки')

    class Meta:
        ordering = ('start_time', )


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(
        regex=r'^7[0-9]{10,10}$')],
        verbose_name='номер телефона клиента')
    operator_code = models.CharField(max_length=3, validators=[
                RegexValidator(regex=r'^[0-9]{3,3}$')],
        verbose_name='код мобильного оператора')
    tag = models.CharField(max_length=50, verbose_name='произвольная метка')
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC', verbose_name='часовой пояс')

    class Meta:
        ordering = ('phone_number', )

    def __str__(self):
        return self.tag


class Message(models.Model):
    STATUSES = [('is_planned', 'planned'),
                ('is_sent', 'sent'),
                ('is_delivered', 'delivered'),
                ('error', 'error')]
    creation_time = models.DateTimeField(verbose_name='время создания')
    status = models.CharField(max_length=50, choices=STATUSES,
                              verbose_name='статус отправки')
    mailout = models.ForeignKey(MailOut, on_delete=models.CASCADE,
                                related_name='messages',
                                verbose_name='id рассылки')
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               related_name='messages',
                               verbose_name='id клиента')

    class Meta:
        ordering = ('-creation_time', )

    def __str__(self):
        return self.status
