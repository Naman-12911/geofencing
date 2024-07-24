from django.urls import path,include
from .views import *


urlpatterns = [
     path('shift-booking/', ShiftBookingAPIview.as_view(),name="ShiftBookingAPIview"),
     path('check-in-check-out/', CheckInCheckOutAPIview.as_view(),name="CheckInCheckOutAPIview"),
]