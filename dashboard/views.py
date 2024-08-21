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


# Check if the user is a superuser
# @user_passes_test(lambda u: u.is_superuser)
# def manage_profiles(request):
#     profiles = Profile.objects.all()
#     context = {
#         'profiles': profiles,
#     }
#     return render(request, 'dashboard/manage_profiles.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def toggle_superuser(request, profile_id):
#     profile = get_object_or_404(Profile, id=profile_id)
#     user = profile.user
#     user.is_superuser = not user.is_superuser
#     user.save()
#     return redirect('dash-manage_profiles')
