# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

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
    products = Product.objects.all()

    context = {
        'products': products,
        # 'form': form,
        # 'customer_count': customer_count,
        # 'product_count': product_count,
        # 'order_count': order_count,
    }
    return render(request,'dashboard/product.html', context)

#Request for viewing staff page via render
@login_required
def order(request):
    return render(request,'dashboard/order.html')
