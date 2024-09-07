from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Event_up

# Create your views here.

@login_required
def dash(request):
    recent_posts = Post.objects.order_by('-date_posted')[:5]
    
    upcoming_events = Event_up.objects.filter(status='Scheduled').order_by('date')
    
    context = {
        'posts': recent_posts,
        'upcoming_events': upcoming_events
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def payment(request):
    return render(request, 'dashboard/payment.html')

@login_required
def status(request):
    return render(request, 'dashboard/status.html')


