from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Products
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import Registration


# Products.objects.all() return all the products in the database


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html')


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('last_name')  # to get username in the form
            messages.success(request, 'un compte est crée pour ' + user)
            print("User is been successfully created")
            return redirect('login')
        else:
            messages.info(request, "Les mots de passe sont differents")
            print("Password are not matching")
    else:
        print("Form ain't valid")
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("User is none")
            print(username)
            messages.info(request, "nom d'utilisateur ou mot de passe est incorrect")
    else:
        print("This is not a post method")
    return render(request, 'login.html')


@login_required
def home(request):
    travaux = Registration.objects.all()
    return render(request, 'home.html', {'travaux': travaux})


def logoutUser(request):
    logout(request)
    return redirect('login')


def taches(request):
    taches = Registration.objects.all()
    return render(request, 'taches.html', {'taches': taches})


def services(request):
    pass
