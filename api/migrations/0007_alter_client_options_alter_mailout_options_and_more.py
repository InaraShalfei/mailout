# Generated by Django 4.0.2 on 2022-03-02 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_message_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='mailout',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('id',)},
        ),
    ]