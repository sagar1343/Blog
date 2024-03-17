from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from .models import BlogPost, Category
# Create your views here.


def home(request):
    categorys = list(Category.objects.all())
    blogs = list(BlogPost.objects.all())
    return render(request=request, template_name='home.html', context={'blogs': blogs, 'categorys': categorys})


def yourposts(request):
    return render(request=request, template_name='yourpost.html')


def logout_user(request):
    logout(request=request)
    messages.success(request=request, message="Logout successfully")
    return redirect(to='home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request=request, message="LogIn successfully")
            return redirect(to='home')
        else:
            form = LoginForm()
            messages.error(request=request, message="Invalid User")
            return render(request=request, template_name='login.html', context={'form': form})
    else:
        form = LoginForm()
        return render(request=request, template_name='login.html', context={'form': form})


def profile(request):
    return render(request=request, template_name='profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(
                request=request, username=username, password=password)
            login(request=request, user=user)
            messages.success(
                request=request, message="Profile created successfully")
            return redirect('home')
        else:
            messages.error(request=request, message="Invalid Form")
            return render(request=request, template_name='register.html', context={'form': form})

    else:
        form = RegistrationForm()
        return render(request=request, template_name='register.html', context={'form': form})
