from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ecom.models import Customer
from django.forms import ModelForm

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'image']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']