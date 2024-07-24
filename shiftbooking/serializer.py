from rest_framework import fields, serializers
from .models import *


    
class ShiftBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftBooking
        fields = "__all__"
    def get_user(self, instance):
        return instance.user.name if instance.user else None

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = self.get_user(instance)
        return response


class CheckInCheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckInCheckOut
        fields = "__all__"
    def get_user(self, instance):
        return instance.user.name if instance.user else None

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = self.get_user(instance)
        return response
    

class GeoFencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoFencing
        fields = "__all__"
    def get_user(self, instance):
        return instance.user.name if instance.user else None

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = self.get_user(instance)
        return response
    
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
    def get_user(self, instance):
        return instance.user.name if instance.user else None

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = self.get_user(instance)
        return response