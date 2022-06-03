from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Student, Group
from main.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):     # переопределение возвращения объектов
        pk = self.kwargs.get("pk")
        if not pk:
            return Student.objects.all()

        return Student.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)   # добавление нового маршрута в ModelViewSet
    def group(self, request, pk=None):
        groups = Group.objects.get(pk=pk)
        return Response({'groups': groups.name})

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
