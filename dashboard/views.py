# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Request for viewing index page via render
def index(request):
    return render(request,'dashboard/index.html')

#Request for viewing staff page via render
def staff(request):
    return render(request,'dashboard/staff.html')

#Request for viewing staff page via render
def product(request):
    return render(request,'dashboard/product.html')

#Request for viewing staff page via render
def order(request):
    return render(request,'dashboard/order.html')
