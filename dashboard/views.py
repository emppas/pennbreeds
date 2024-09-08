from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Event_update
from users.models import FinancialRecord

# Create your views here.

@login_required
def dash(request):
    recent_posts = Post.objects.order_by('-date_posted')[:5]
    
    upcoming_events = Event_update.objects.order_by('date')
    
    try:
        financial_record, created = FinancialRecord.objects.get_or_create(user=request.user)
    except FinancialRecord.DoesNotExist:
        financial_record = None
    
    context = {
        'posts': recent_posts,
        'upcoming_events': upcoming_events,
        'financial_record': financial_record,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def payment(request):
    return render(request, 'dashboard/payment.html')

@login_required
def status(request):
    return render(request, 'dashboard/status.html')


