from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def dash(request):
    return render(request, 'dashboard/index.html')


@login_required
def payment(request):
    return render(request, 'dashboard/payment.html')

@login_required
def status(request):
    return render(request, 'dashboard/status.html')