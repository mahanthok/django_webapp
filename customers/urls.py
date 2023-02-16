from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.home, name='home'),

    path('customer_view/<int:pk>/', views.customer_view, name='customer_view'),
    path('customer_new', views.customer_create, name='customer_new'),
    path('customer_edit/<int:pk>/', views.customer_update, name='customer_edit'),
    path('customer_delete/<int:pk>/', views.customer_delete, name='customer_delete'),

    path('address_new/<int:parent_pk>/', views.address_create, name='address_new'),
    path('address_edit/<int:pk>/', views.address_update, name='address_edit'),
    path('address_delete/<int:pk>/', views.address_delete, name='address_delete'),
]
