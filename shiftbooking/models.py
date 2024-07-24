from django.db import models
from account.models import User
# Create your models here.

class ShiftBooking(models.Model):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    shedule = models.DateField(null=True)
    shedule_confirm = models.BooleanField(default=False)


class CheckInCheckOut(models.Model):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    check_in_time = models.DateTimeField(null=True,blank=True)
    check_out_time = models.DateTimeField(null=True,blank=True)


