from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Student
from main.serializers import StudentSerializer

class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentApiView(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPIList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentAPIUpdate(generics.UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

