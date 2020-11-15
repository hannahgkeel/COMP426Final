from django.contrib import admin
from .models import WaitlistTicket
import datetime

# Register your models here.
#To go back replace 'time_of_check_in' with 'check_in_time' on list_display, and then delete the time_of_check_in() function.
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('customer', 'party_size', 'check_in_time', 'table_is_ready', 'location', 'customer_is_served')
    list_filter = ('location', 'customer_is_served')
    ordering = ('check_in_time',)
    list_editable=('table_is_ready','customer_is_served')
        
admin.site.register(WaitlistTicket, WaitlistAdmin)