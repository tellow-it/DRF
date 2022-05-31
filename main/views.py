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

class StudentApiView(APIView):
    def get(self, request):
        s = Student.objects.all()
        return Response({'students': StudentSerializer(s, many=True).data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Student.objects.create(
            number=request.data['number'],
            name=request.data['name'],
            surname=request.data['surname'],
            father=request.data['father'],
            time_enter=request.data['time_enter'],
            group_id=request.data['group_id'],
            score=request.data['score']
        )
        return Response({'post': StudentSerializer(post_new).data})
