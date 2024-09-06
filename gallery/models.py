from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Sports & Recreation', 'Sports & Recreation'),
        ('Inductions', 'Inductions'),
        ('Award Nites', 'Award Nites'),
        ('Courtesy Visits', 'Courtesy Visits'),
        ('Club Retreats', 'Club Retreats'),
        ('Burials', 'Burials'),
        ('Monthly Meetings', 'Monthly Meetings'),
    ]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=False, null=True)
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f'Image for {self.event.title}'
