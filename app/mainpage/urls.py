from django.urls import path
from .views import index, order_create


urlpatterns = [
	path('', index),
    path('api/order/create', order_create, name='order_create'),
]