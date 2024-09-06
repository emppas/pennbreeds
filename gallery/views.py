from django.shortcuts import render, get_object_or_404
from .models import Event, Image

# Create your views here.


def category_list(request):
    # Get all distinct categories from Event model
    categories = Event.objects.values_list('category', flat=True).distinct()
    
     # Get all images for the "All" tab
    # all_images = Image.objects.all()
    
    # Create a dictionary to hold images by category
    category_images = {}
    for category in categories:
        category_images[category] = Image.objects.filter(event__category=category)
    
       
    return render(request, 'gallery/category_list.html', {
        'categories': categories,
        'category_images': category_images,
        # 'all_images': all_images,  # Pass all images to the "All" tab
    })




def event_list(request, category_name):
    events = Event.objects.filter(category=category_name)
    return render(request, 'gallery/event_list.html', {'category': category_name, 'events': events})





def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    images = event.images.all()
    return render(request, 'gallery/event_detail.html', {'event': event, 'images': images})
