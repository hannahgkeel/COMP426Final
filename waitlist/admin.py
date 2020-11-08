from django.contrib import admin
from .models import WaitlistTicket

# Take care of the next customer:
def notify_selected_customers(modeladmin, request, queryset):
    queryset.delete()
    notify_selected_customers.short_description= "Notify selected customers"

# Register your models here.
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('customer', 'party_size', 'check_in_time', 'location')
    list_filter = ('location',)
    ordering = ('check_in_time',)
    actions = [notify_selected_customers]


admin.site.register(WaitlistTicket, WaitlistAdmin)
