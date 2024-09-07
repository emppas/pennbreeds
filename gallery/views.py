from django.shortcuts import render
from .models import Event, Image

def category_list(request):
    # Get all distinct categories from Event model
    categories = Event.objects.values_list('category', flat=True).distinct()
    
    # Create a dictionary to hold images by category
    category_images = {}
    for category in categories:
        images = Image.objects.filter(event__category=category)
        category_images[category] = images
    
    # Set the default category
    default_category = categories[3] if categories else None
    
    return render(request, 'gallery/category_list.html', {
        'categories': categories,
        'category_images': category_images,
        'default_category': default_category
    })
