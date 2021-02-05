from django.shortcuts import render, redirect
from .forms import CreateUser, CustomerForm, UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ecom.models import Customer, Order, Item

# Create your views here.
def register_user(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            form.save()
            messages.success(request, f'Sign up successful, Login as {name}')
            return redirect('login')
    context = {
        'title': 'Sign Up',
        'form': form,
    }
    return render(request, 'user/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            messages.warning(request, 'Invalid Username or Password')
    return render(request, 'user/login.html', {'title': 'Login'})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = Customer.objects.get(customer=request.user)
    form1 = CustomerForm(instance=user)
    form2 = UserForm(instance=request.user)
    if request.method == 'POST':
        form1 = CustomerForm(request.POST, request.FILES, instance=user)
        form2 = UserForm(request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            messages.success(request, 'Profile updated')
            form1.save()
            form2.save()
        else:
            raise Exception
    return render(request, 'user/profile.html', { 'user': user, 'title': 'Profile', 'form1': form1, 'form2': form2 })

@login_required
def cart(request):
    orders = Order.objects.filter(customer=request.user.customer).order_by('-date_created')
    return render(request, 'user/cart.html', { 'title': 'Cart', 'orders': orders })

@login_required
def remove_cart(request, id):
    order = Order.objects.filter(id=id)
    order.delete()

    return redirect('cart')

@login_required
def add_to_cart(request, id):
    item = Item.objects.get(id=id)
    order = Order(customer=request.user.customer, item=item)
    order.save()

    return redirect('cart')
