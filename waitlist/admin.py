from django.contrib import admin
from .models import WaitlistTicket

# Take care of the next customer:
def notify_customer(modeladmin, request, queryset):
    queryset.delete()
    notify_customer.short_description= "Notify customer(s) table is ready"

# Register your models here.
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('customer', 'party_size', 'check_in_time', 'location')
    list_filter = ('location',)
    actions = [notify_customer]


admin.site.register(WaitlistTicket, WaitlistAdmin)
