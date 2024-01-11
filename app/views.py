from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.forms import *

def Create_Student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Student data created')
        return HttpResponse('Student data not created')
    return render(request,'Create_Student.html',d)