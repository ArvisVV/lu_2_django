from django.db import models


class Student(models.Model):
    name = models.TextField()
    average_grade = models.FloatField()

    def __str__(self):
        return self.name
