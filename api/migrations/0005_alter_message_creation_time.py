# Generated by Django 4.0.2 on 2022-03-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_message_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время создания'),
        ),
    ]
