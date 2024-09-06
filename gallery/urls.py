from django.urls import path
from . import views



urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('events/<str:category_name>/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]