# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

#Request for viewing index page via render
@login_required
def index(request):
    return render(request,'dashboard/index.html')

#Request for viewing staff page via render
@login_required
def staff(request):
    return render(request,'dashboard/staff.html')

#Request for viewing staff page via render
@login_required
def product(request):
    return render(request,'dashboard/product.html')

#Request for viewing staff page via render
@login_required
def order(request):
    return render(request,'dashboard/order.html')
