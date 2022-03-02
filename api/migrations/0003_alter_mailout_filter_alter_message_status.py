# Generated by Django 4.0.2 on 2022-03-02 06:05

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_client_operator_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailout',
            name='filter',
            field=models.JSONField(default=dict, validators=[api.validators.JSONSchemaValidator(limit_value={'properties': {'operator_code': {'type': 'string'}, 'tag': {'type': 'string'}}, 'type': 'object'})], verbose_name='фильтр свойств рассылки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('is_planned', 'planned'), ('is_sent', 'sent'), ('is_delivered', 'delivered'), ('cancelled', 'cancelled'), ('error', 'error')], max_length=50, verbose_name='статус отправки'),
        ),
    ]