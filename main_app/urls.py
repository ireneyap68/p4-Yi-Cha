from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('about/', views.about, name='about'),
    path('cart/', views.product_details, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]