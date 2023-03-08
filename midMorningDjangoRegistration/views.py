from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Supplier


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('register')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_product(request):
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Start receiving data from the form
        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST.get('bei')

        # Finally save the data in our table called products
        product = Product(prod_name=p_name, prod_quantity=p_quantity, prod_price=p_price)
        product.save()
        # Redirect back with a success message
        messages.success(request, 'Product saved successfully')
        return redirect('add-product')

    return render(request, 'add-product.html')


@login_required
def view_products(request):
    # Select the products to be displayed
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required
def delete_product(request, id):
    # Fetch the product to be deleted
    product = Product.objects.get(id=id)
    # Delete the product
    product.delete()
    # Redirect back to products page with a message
    messages.success(request, 'Product deleted successfully')
    return redirect('products')


@login_required
def update_product(request, id):
    # Fetch the product to be updated
    product = Product.objects.get(id=id)
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Receive data from the form
        updated_name = request.POST.get('jina')
        updated_quantity = request.POST.get('kiasi')
        updated_price = request.POST.get('bei')

        # Update the product with the received updated data
        product.prod_name = updated_name
        product.prod_quantity = updated_quantity
        product.prod_price = updated_price

        # Return the data back to the database and redirect back
        # to products page with a success message
        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect('products')

    return render(request, 'update-product.html', {'product': product})


@login_required
def payment(request, id):
    # Select the product to be paid
    product = Product.objects.get(id=id)
    return render(request, 'payment.html', {'product': product})









def view_supplier(request):
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Start receiving data from the form
        sup_name = request.POST.get('jina')
        sup_email = request.POST.get('pepe')
        sup_phone = request.POST.get('nambari')
        sup_product = request.POST.get('vitu')

        # Finally save the data in our table called products
        supplier = Supplier(sup_name=sup_name, sup_email=sup_email, sup_product=sup_product, sup_phone=sup_phone)
        supplier.save()
        # Redirect back with a success message
        messages.success(request, 'supplier saved successfully')
        return redirect('view_suppliers')

    return render(request, 'suppliers.html')


@login_required
def delete_supplier(request, id):
    # Fetch the product to be deleted
    product = Product.objects.get(id=id)
    # Delete the product
    product.delete()
    # Redirect back to products page with a message
    messages.success(request, 'Supplier deleted successfully')
    return redirect('suppliers')


@login_required
def update_supplier(request, id):
    # Fetch the product to be updated
    product = Product.objects.get(id=id)
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Receive data from the form
        updated_name = request.POST.get('jina')
        updated_email = request.POST.get('pepe')
        updated_phone = request.POST.get('nambari')
        updated_product = request.POST.get('vitu')

        # Update the product with the received updated data
        Supplier.sup_name = updated_name
        Supplier.sup_email = updated_email
        Supplier.sup_phone = updated_phone
        Supplier.sup_product = updated_product

        # Return the data back to the database and redirect back
        # to products page with a success message
        product.save()
        messages.success(request, 'Supplier updated successfully')
        return redirect('update-supplier')

    return render(request, 'view-suppliers.html', {'supplier': Supplier})
