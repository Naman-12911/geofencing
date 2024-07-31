from django.db import models
from account.models import User
from django.utils import timezone
# Create your models here.

class ShiftBooking(models.Model):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    shedule = models.DateField(null=True)
    shedule_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)


class CheckInCheckOut(models.Model):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    check_in_time = models.DateTimeField(null=True,blank=True)
    check_out_time = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)


class GeoFencing(models.Model):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    cordinates = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)
