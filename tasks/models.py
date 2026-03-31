from django.db import models
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}  {self.club.name}"
