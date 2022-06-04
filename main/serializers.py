import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Student
        fields = '__all__'
