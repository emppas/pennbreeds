from django.contrib import admin
from .models import Profile, Execo

# Register your models here.

admin.site.register(Profile)


# Define a custom admin class for the Execo model
class ExecoAdmin(admin.ModelAdmin):
    # List display fields
    list_display = ('user', 'name', 'title', 'position')
    
    # Read-only fields
    readonly_fields = ('name', 'title')

    # Fields to display in the form
    fields = ('user', 'name', 'title', 'position')

    # Custom form for the admin panel
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields
        return self.readonly_fields

# Register the Execo model with the custom admin class
admin.site.register(Execo, ExecoAdmin)