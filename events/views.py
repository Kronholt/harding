from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .filters import PostFilter
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm, CreateUserForm
from .models import *
from django.contrib import messages
import requests
import json

# Create your views here.
def index(request):
    response = requests.get('http://hardingdevelopment.nexisit.net/harding_api/api_event_search.php?page_num=0&per_page=20&buckets=Volunteering&timezone=25200&app_server_version=3.2&app_version=2&app_build=1&user_id=2&token=70aedda35dca9c192ef551c9f7b570e0&salt=309a9bea4d2695656e83f4fe7b340ee0&app=1&version=3.2').json()

    return render(request, 'events/home.html', {'response':response})


def volunteering(request):
    posts = Post.objects.filter(post_type='Event')
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    context={'posts':posts, 'myFilter':myFilter}
    return render(request, 'events/volunteering.html', context)

def event(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm()
    context = {'post':post, 'form':form}
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user.volunteer
            post.comment_set.add(comment)
            comment.save()
            return redirect('event', pk)
    return render(request,'events/event.html', context )

def attend(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    post.attending.add(user)
    post.save()
    return redirect('/')
    

def stories(request):
    posts = Post.objects.filter(post_type='Story')
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    context={'posts':posts, 'myFilter':myFilter}
    return render(request, 'events/stories.html', context)

def story(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm()
    context = {'post':post, 'form':form}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user.volunteer
            post.comment_set.add(comment)
            comment.save()
            return redirect('story', pk)
    return render(request,'events/story.html', context)

def register(request):
    #this functionality stops a user from visiting register while logged int
    form = CreateUserForm()
    context={'form':form}
    template = 'events/register.html'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            volunteer = Volunteer(user=user, user_name=user.username)
            volunteer.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('/')
        else:
            messages.error(request, 'Something went wrong, please try again.')
    return render(request, template, context)


def loginPage(request):
    form=UserCreationForm()
    context={'form':form}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password is incorrect')
    template = 'events/login.html'
    return render(request, template, context)