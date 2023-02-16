from django.forms import ModelForm

from .models import Customer, Address

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'age']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'country']