from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact Us!'})


def blog(request):
    context = {
        'title': 'Blog Page',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)


def members(request):
    profiles = Profile.objects.all().order_by('id')[1:]
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


def post_detail(request):
     return render(request, 'blog/post_detail.html', {'title': 'Post Details Page'})
    

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        
        # Create a new post object
        post = Post(
            title=title,
            content=content,
            category=category,
            image=image,
            author=request.user
        )
        post.save()
        
        return redirect('blog-blog') # Redirect to the blog or post list page
    
    # Pass category choices to the template
    categories = Post.CATEGORY_CHOICES
    context = {
        'categories': categories
    }
    return render(request, 'blog/create_post.html', context)