from django.contrib import admin
from .models import WaitlistTicket

# Register your models here.
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('customer', 'party_size', 'checkin_date', 'location')
    list_filter = ('location',)


admin.site.register(WaitlistTicket, WaitlistAdmin)
