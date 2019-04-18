from django.db import models
from faker import Faker


faker = Faker()
class Client(models.Model):
    name = models.CharField(max_length=30)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.name())

class Hotel(models.Model):
    name = models.CharField(max_length=30)
    clients = models.ManyToManyField(Client, related_name='hotel')

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.company())


class Student(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Lecture(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.title}'


class Enroll(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.student.id} {self.lecture.id}'