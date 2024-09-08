from django.contrib import admin
from .models import Profile, Execo
from .models import FinancialRecord

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




class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_fee_due', 'total_amount_due', 'total_amount_owed', 'overall_debt', 'last_payment_date', 'payment_status', 'balance_owing')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_filter = ('payment_status',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

admin.site.register(FinancialRecord, FinancialRecordAdmin)
