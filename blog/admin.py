from django.contrib import admin
from .models import Post
from .models import Event_update

# Register your models here.

admin.site.register(Post)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'venue', 'status')
    list_filter = ('status', 'date')
    search_fields = ('name', 'venue')
    ordering = ('-date',) 

admin.site.register(Event_update, EventAdmin)