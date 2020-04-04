from django.urls import path

urlpatterns = [
    path('', list_products, name='list_products'),
]