from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

LOCATION_CHOICES = (
    ('Carrboro', 'Carrboro'),
    ('Chapel Hill', 'Chapel Hill'),
)

# Create your models here.
class WaitlistTicket(models.Model):

    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    check_in_time = models.TimeField(auto_now=True)
    party_size = models.IntegerField()
    customer = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #table_is_ready = models.BooleanField(default=False)
    #customer_is_served = models.BooleanField(default=False)

    def __str__(self):
        return self.customer
