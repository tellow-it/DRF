from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import *
from main.models import Student, Group
from main.serializers import StudentSerializer


class StudentAPIList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # для авторизованных ползователей


class StudentAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class StudentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminOrReadOnly,)  # только для администратора


