from django.contrib import admin

from api.models import MailOut, Client, Message


class MailOutAdmin(admin.ModelAdmin):
    list_filter = ('start_time', 'finish_time',)


class ClientAdmin(admin.ModelAdmin):
    list_filter = ('tag', 'operator_code', 'timezone',)


class MessageAdmin(admin.ModelAdmin):
    list_filter = ('status',)


admin.site.register(MailOut, MailOutAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)
