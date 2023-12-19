from django.contrib import admin

from .models import *


class BankCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'firstname_surname',)
    list_display_links = ('id', 'number')
    search_fields = ('firstname_surname',)
    list_filter = ('number',)


admin.site.register(BankCard, BankCardAdmin)
