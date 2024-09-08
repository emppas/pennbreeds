from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('members/', views.members, name='blog-members'),
    path('search/', views.member_search, name='member-search'),
    path('blog/', views.blog, name='blog-blog'),
    path('execos/', views.execo_list, name='blog-execos'),
    path('blog/post-details/', views.post_detail, name='post-details'),
    path('post/new/', views.create_post, name='create_post'),
    
]