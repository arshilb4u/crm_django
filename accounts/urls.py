from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('create_order/',views.createorder,name='create_order'),
    path('update_order/<str:pk>',views.updateorder,name='update_order')
]
