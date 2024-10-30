from django.shortcuts import render
from apps.main.models import My_student
# Create your views here.
def index(request):
    students = My_student.objects.all()
    return render(request,'index.html',locals())