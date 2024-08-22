from django.db import models
from django.contrib.auth.models import User
from PIL import Image as PILImage
import os

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_approved = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.user.username} Profile'
   
 
class Execo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        # Automatically fill the title and name based on the user's profile
        if self.user and hasattr(self.user, 'profile'):
            self.title = self.user.profile.title
        if self.user:
            self.name = f'{self.user.first_name} {self.user.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.position}'