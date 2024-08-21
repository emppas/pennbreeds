from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dash, name='dash-index'),
    path('payment/', views.payment, name='dash-payment'),
    path('status/', views.status, name='dash-status'),
       
    
]






# from django.urls import path
# from . import views


# urlpatterns = [
#     path('dashboard/', views.dash, name='dash-index'),
#     path('payment/', views.payment, name='dash-payment'),
#     path('status/', views.status, name='dash-status'),
# ]
