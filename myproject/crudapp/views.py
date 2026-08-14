from django.shortcuts import render,redirect    
from .forms import ProductForm,RegisterForm
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')
#R-read-fetch data from db and display in admin dashboard   
def  admin(request):
    products=Product.objects.all()
    return render(request, 'admin_dashboard.html',{'products': products})
#create-add data to db using forms
def add_product(request):
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form=ProductForm()
    return render(request, 'addproduct.html',{'form': form})
#D-delete data from db
def delete_product(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    return redirect('products')
#u-update existing data in db
def update_product(request,id):
    product=get_object_or_404(Product,id=id)
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else :
        form=ProductForm(instance=product)
    return render(request,'addproduct.html',{'form':form})
#registering a user
def register_user(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()#saves to db the user
            return redirect('index')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
    

