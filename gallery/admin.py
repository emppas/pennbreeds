from django.contrib import admin
from .models import Event, Image

class EventImageInline(admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True  # Allow deletion of individual images

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)
