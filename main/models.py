from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Student(models.Model):
    number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    time_enter = models.DateTimeField()
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, max_length=50)
    score = models.PositiveIntegerField(default=2)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.surname + self.father


class Group(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    number = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.name + str(self.number)
