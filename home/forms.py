from django import forms
from models import *

class Customer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','contact' , 'email' , 'password' , 'city' ,'state']