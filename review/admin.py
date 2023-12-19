from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('description','estimate',)
    list_display_links = ('description','estimate',)
    search_fields = ('description',)
    list_filter = ('description',)


admin.site.register(Review, ReviewAdmin)
