from django.contrib import admin
from .models import Audio
# Register your models here.

class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('id', 'title', 'author')

admin.site.register(Audio, AudioAdmin)