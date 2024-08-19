from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.Field()
    last_name = forms.Field()
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['title', 'image']