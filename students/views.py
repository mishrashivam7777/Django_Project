from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def index(request):
    return render(request, 'index.html',{'students':Student.objects.all()})
