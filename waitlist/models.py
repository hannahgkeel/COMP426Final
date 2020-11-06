from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class WaitlistTicket(models.Model):
    location = models.CharField(max_length=50)
    checkin_date = models.DateTimeField(default=datetime.now, blank=True)
    party_size = models.IntegerField()
    customer = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer
