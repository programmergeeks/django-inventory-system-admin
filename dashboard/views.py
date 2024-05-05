from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Request for viewing index page via HttpResponse
def index(request):
    return render(request,'index.html')

#Request for viewing staff page via HttpResponse
def staff(request):
    return render(request,'staff.html')
