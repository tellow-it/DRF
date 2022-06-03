from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Student
from main.serializers import StudentSerializer


# class StudentApiView(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentAPIList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentApiView(APIView):
    def get(self, request):
        s = Student.objects.all()
        return Response({'students': StudentSerializer(s, many=True).data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT npt allowed"})

        try:
            instance = Student.objects.get(pk=pk)
        except:
            return StudentSerializer({"error": "Object does not exists"})

        serializer = StudentSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            student_del = Student.objects.get(pk=pk)
        except:
            return StudentSerializer({"error": "Object does not exists"})

        student_del.delete()
        return Response({"message": "Success delete"})
