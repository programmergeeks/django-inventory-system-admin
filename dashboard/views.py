# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

#Request for viewing index page via render
@login_required
def index(request):
    employee = User.objects.all()
    orders = Order.objects.all()
    product = Product.objects.all()

    employee_count = employee.count()
    product_count = product.count()
    order_count = orders.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.staff = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'product': product,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count
    }
    return render(request,'dashboard/index.html', context)

#Request for viewing staff page via render
@login_required
def staff(request):
    employee = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    employee_count = employee.count()
    product_count = products.count()
    order_count = orders.count()
    
    context = {
        'employee': employee,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count
    }

    return render(request,'dashboard/staff.html', context)

def staff_detail(request, pk):
    employee = User.objects.get(id=pk)
    context = {
        'employee': employee
    }

    return render(request,'dashboard/staff_detail.html', context)

#Request for viewing staff page via render
@login_required
def product(request):
    employee = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    employee_count = employee.count()
    product_count = products.count()
    order_count = orders.count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
        
    context = {
        'products': products,
        'form': form,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request,'dashboard/product.html', context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)

def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:

        form = ProductForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)



#Request for viewing staff page via render
@login_required
def order(request):
    employee = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    employee_count = employee.count()
    product_count = products.count()
    order_count = orders.count()

    context = {
        'orders': orders,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count,
    }

    return render(request, 'dashboard/order.html', context)
