import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Student
from rest_framework import serializers


# class StudentModel:
#     def __init__(self, number, name, surname, father,score):
#         self.number = number
#         self.name = name
#         self.surname = surname
#         self.father = father
#         self.score = score


class StudentSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    father = serializers.CharField(max_length=100)
    time_enter = serializers.DateTimeField()
    group_id = serializers.IntegerField()  # json! поэтму не ForeighKey
    score = serializers.IntegerField(default=2)

# кодирование
# def encode():
#     model = StudentModel(845432, 'I', 'T', 'A', 5)
#     model_sr = StudentSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# # декодирование
# def decode():
#     stream = io.BytesIO(b'{"number":845432,"name":"I","surname":"T","father":"A","score":5}')
#     data = JSONParser().parse(stream)
#     serializer = StudentSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
