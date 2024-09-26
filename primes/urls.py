from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='input_page'),
    path('primes/', views.prime_number, name='output_page'),
]

