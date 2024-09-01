from django.shortcuts import render
from .models import Post
from users.models import Profile, Execo
from django.core.paginator import Paginator
from django.http import HttpResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})


def blog(request):
    context = {
        'title': 'Blog Page',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)


def members(request):
    profiles = Profile.objects.all().order_by('id')[2:]
    paginator = Paginator(profiles, 8)  # Show 8 profiles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'title': 'Welcome to Club Members Page',
        'page_obj': page_obj,
    }

    return render(request, 'blog/members.html', context)

def member_search(request):
    query = request.GET.get('q', '')
    profiles = Profile.objects.filter(
        user__first_name__icontains=query
    ) | Profile.objects.filter(
        user__last_name__icontains=query
    )
    return render(request, 'blog/partials/_member_list.html', {'profiles': profiles})

def execo_list(request):
    execos = Execo.objects.all()
    context = {
        'execos' : execos,
    }
    return render(request, 'blog/execo_list.html', context)

def blog_post(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'title': 'Welcome to Blog Post Page',
        'posts': page_obj,
    }
    return render(request, 'blog/article.html', context)