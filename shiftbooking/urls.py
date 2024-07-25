from django.urls import path,include
from .views import *


urlpatterns = [
     path('shift-booking/', ShiftBookingAPIview.as_view(),name="ShiftBookingAPIview"),
     path('shift-booking/<int:pk>/', ShiftBookingAPIview.as_view(),name="ShiftBookingAPIview"),
     path('check-in-check-out/', CheckInCheckOutAPIview.as_view(),name="CheckInCheckOutAPIview"),
     path('check-in-check-out/<int:pk>/', CheckInCheckOutAPIview.as_view(),name="CheckInCheckOutAPIview"),
     path('geo-fencing/', GeoFencingAPIview.as_view(),name="GeoFencingAPIview"),
     path('geo-fencing/<int:pk>/', GeoFencingAPIview.as_view(),name="GeoFencingAPIview"),
     path('notification/', NotificationAPIview.as_view(),name="NotificationAPIview"),
     path('notification/<int:pk>/', NotificationAPIview.as_view(),name="NotificationAPIview"),
]