from django.urls import path
from . import views



urlpatterns = [
    path('gallery/categories/', views.category_list, name='category_list'),
  
]