from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store, name='store'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),

]
