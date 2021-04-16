from django.shortcuts import render

from students.student import Student
from students import models


def index(request):
    return render(
        request=request,
        template_name='students/index.html',
    )


def average(request):
    name = request.POST['name']
    grades = list(map(int, request.POST['grades'].split(',')))

    named_student = Student(
        name=name,
        grades=grades,
    )

    student_average = named_student.average()

    student = models.Student(
        name=named_student.name,
        average_grade=student_average,
    )

    student.save()

    return render(
        request=request,
        template_name='students/average.html',
        context={
            'student_name': named_student.name,
            'student_average': student_average,
        }
    )
