from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Tech', 'Tech'),
        ('Politics', 'Politics'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('History', 'History'),
        ('Entertainment', 'Entertainment'),
        ('Style', 'Style')
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Politics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='blog_imgs/', blank=False, null=False)
   
   
    
    def __str__(self):
        return self.title


class Event_update(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    name = models.CharField(max_length=60)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Scheduled')
    
    def __str__(self):
        return f"{self.name} at {self.venue} on {self.date.strftime('%Y-%m-%d')} - {self.status}"