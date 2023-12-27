from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('produk/', views.data_produk, name='produk'),
    path('hapus_produk/<produk_id>', views.hapus_produk, name='hapus-produk'),
]