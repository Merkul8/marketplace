from django.contrib import admin
from .models import Customer, Role


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role_id',)
    list_display_links = ('id', 'username')
    search_fields = ('name', 'email',)
    list_filter = ('role_id',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Role)