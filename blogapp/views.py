from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, CreateBlogForm
from .models import BlogPost, Category


def home(request):
    category_id = request.GET.get('category')
    if category_id:
        blogs = BlogPost.objects.filter(category__id=category_id)
        if not blogs.exists():
            messages.info(
                request=request, message="No post in this category ")
    else:
        blogs = BlogPost.objects.all()
    categorys = Category.objects.all()
    return render(request=request, template_name='home.html', context={'blogs': list(blogs.order_by('-date')), 'categorys': list(categorys)})


@login_required
def yourposts(request):
    user = request.user
    blogs = user.blogpost_set.all()
    total_post = blogs.count()
    return render(request=request, template_name='yourpost.html', context={'blogs': list(blogs), 'total_posts': total_post})


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
    author = request.user
    return render(request=request, template_name='profile.html', context={'author': author})


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
            return redirect(to='home')
        else:
            messages.error(request=request, message="Invalid Form")
            return render(request=request, template_name='register.html', context={'form': form})

    else:
        form = RegistrationForm()
        return render(request=request, template_name='register.html', context={'form': form})


@login_required()
def createBlog(request):
    if request.method == 'POST':
        form = CreateBlogForm(data=request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect(to='home')
        else:
            messages.warning(request=request, message="Invalid post")
    else:
        form = CreateBlogForm()
    return render(request=request, template_name='createBlog.html', context={'form': form})
