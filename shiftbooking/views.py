from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http.response import Http404
from rest_framework.response import Response


class ShiftBookingAPIview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return ShiftBooking.objects.get(pk=pk)
        except ShiftBooking.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
            if pk:
                data = ShiftBooking.objects.all()
                serializer = ShiftBookingSerializer(data)
                return Response(serializer.data)

            else:
                data = ShiftBooking.objects.all()
                serializer = ShiftBookingSerializer(data, many=True)

                return Response(serializer.data)
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id 
            
            serializer = ShiftBookingSerializer(data=mutable_data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # Return Response to User

            response = Response()

            response.data = {
                'message': 'shift booking saved Successfully',
                'data': serializer.data
            }
            return response

    def patch(self, request, pk=None, format=None):
        # Get the todo to update
        shift_to_update = ShiftBooking.objects.get(pk=pk)

        serializer = ShiftBooking(instance=shift_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = {
            'message': 'Shif tBooking updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        shift_to_delete =  ShiftBooking.objects.get(pk=pk)

            # delete the todo
        shift_to_delete.delete()

        return Response({
            'message': 'Shift Booking Deleted Successfully'
        })
    


class CheckInCheckOutAPIview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return CheckInCheckOut.objects.get(pk=pk)
        except CheckInCheckOut.DoesNotExist:
            raise Http404
        
    def get(self, request, pk=None, format=None):
            if pk:
                data = CheckInCheckOut.objects.all()
                serializer = CheckInCheckOutSerializer(data)
                return Response(serializer.data)

            else:
                data = CheckInCheckOut.objects.all()
                serializer = CheckInCheckOutSerializer(data, many=True)

                return Response(serializer.data)
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id 
            
            serializer = CheckInCheckOutSerializer(data=mutable_data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # Return Response to User

            response = Response()

            response.data = {
                'message': 'Check In Check Out saved Successfully',
                'data': serializer.data
            }
            return response

    def patch(self, request, pk=None, format=None):
        # Get the todo to update
        shift_to_update = CheckInCheckOut.objects.get(pk=pk)

        serializer = CheckInCheckOutSerializer(instance=shift_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = {
            'message': 'Check In Check Outupdated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        shift_to_delete =  CheckInCheckOut.objects.get(pk=pk)

            # delete the todo
        shift_to_delete.delete()

        return Response({
            'message': 'Check In Check Out Deleted Successfully'
        })