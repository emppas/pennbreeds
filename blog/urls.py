from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('members/', views.members, name='blog-members'),
    path('search/', views.member_search, name='member-search'),
    
    
]