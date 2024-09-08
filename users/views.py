from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            # Check if the profile already exists
            profile, created = Profile.objects.get_or_create(user=user)
            
            # Update the profile with the data from the form
            profile.title = profile_form.cleaned_data['title']
            if profile_form.cleaned_data['image']:
                profile.image = profile_form.cleaned_data['image']
            profile.save()

            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created! You are now able to log in')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/register.html', context)

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.profile.is_approved:
                login(request, user)
                return redirect('blog-home')
            else:
                messages.error(request, 'Your account is not approved yet. Please wait for the admins approvals.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

