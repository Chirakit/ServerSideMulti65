from django.shortcuts import render
from appointments.models import Doctor, Patient, Appointment
from appointments.serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, AppointmentAddSerializer
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from appointments.permissions import AppointmentPermission, AppointmentListPermission

class MyTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"

class DoctorList(APIView):
    authentication_classes = [MyTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class PatientList(APIView):
    authentication_classes = [MyTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

class AppointmentList(APIView):
    authentication_classes = [MyTokenAuthentication]
    permission_classes = [AppointmentListPermission]

    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

class AppointmentDetailList(APIView):
    authentication_classes = [MyTokenAuthentication]
    permission_classes = [IsAuthenticated, AppointmentPermission]

    def get(self, request, appointment_id):
        appointment_detail = Appointment.objects.get(pk=appointment_id)
        serializer = AppointmentSerializer(appointment_detail)
        return Response(serializer.data)

    def put(self, request, appointment_id):
        appointment_detail = Appointment.objects.get(pk=appointment_id)
        self.check_object_permissions(request, appointment_detail)

        serializer = AppointmentAddSerializer(appointment_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, appointment_id):
        appointment_detail = Appointment.objects.get(pk=appointment_id)
        self.check_object_permissions(request, appointment_detail)
        if request.user != appointment_detail.created_by:
            return Response("Only owner can delete.", status=status.HTTP_403_FORBIDDEN)

        appointment_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
