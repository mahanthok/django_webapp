from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Customer, Address
from .forms import CustomerForm, AddressForm


# ========== Home =========

def home(request, template_name='customers/home.html'):
    customers = Customer.objects.all()
    ctx = {
        'customers': customers,
    }
    return render(request, template_name, ctx)
    

# ========== customers CRUD =========

def customer_view(request, pk, template_name='customers/customer_view.html'):
    customer= get_object_or_404(Customer, pk=pk)
    addresses = Address.objects.filter(customer=customer)
    ctx = {
        'customer': customer,
        'addresses': addresses,
    }
    return render(request, template_name, ctx)

def customer_create(request, template_name='customers/customer_form.html'):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customers:home')
    ctx = {
        'form': form,
    }
    return render(request, template_name, ctx)

def customer_update(request, pk, template_name='customers/customer_form.html'):
    customer= get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customers:home')
    ctx = {
        'form': form,
        'customer': customer,
    }
    return render(request, template_name, ctx)

def customer_delete(request, pk, template_name='customers/customer_confirm_delete.html'):
    customer= get_object_or_404(Customer, pk=pk)    
    if request.method=='POST':
        customer.delete()
        return redirect('customers:home')
    ctx = {
        'object': customer,
        'customer': customer,
    }
    return render(request, template_name, ctx)


# ========== Address CRUD =========

def address_create(request, parent_pk, template_name='customers/address_form.html'):
    customer = get_object_or_404(Customer, pk=parent_pk)
    form = AddressForm(request.POST or None)
    if form.is_valid():
        address = form.save(commit=False)
        address.customer = customer
        address.save()
        return redirect('customers:customer_view', parent_pk)
    ctx = {
        'form': form,
        'customer': customer,
    }
    return render(request, template_name, ctx)

def address_update(request, pk, template_name='customers/address_form.html'):
    address = get_object_or_404(Address, pk=pk)
    parent_pk = address.customer.pk
    form = AddressForm(request.POST or None, instance=address)
    if form.is_valid():
        form.save()
        return redirect('customers:customer_view', parent_pk)
    ctx = {
        'form': form,
        'customer': address.customer,
    }
    return render(request, template_name, ctx)

def address_delete(request, pk, template_name='customers/address_confirm_delete.html'):
    address = get_object_or_404(Address, pk=pk)    
    parent_pk = address.customer.pk
    if request.method=='POST':
        address.delete()
        return redirect('customers:customer_view', parent_pk)
    ctx = {
        'object': address,
        'customer': address.customer,
    }
    return render(request, template_name, ctx)
