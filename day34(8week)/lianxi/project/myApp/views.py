from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("sunck is a good man")

from .models import Grades, Students
def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板在渲染页面，将渲染好的页面返回浏览器
    context = {"grades": gradesList}
    return render(request, 'myApp/grades.html',context=context )

def students(request):
    studentsList = Students.objects.all()
    return render(request, 'myApp/students.html', {"students": studentsList})

def studentsGrade(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {"students": studentsList})