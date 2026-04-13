from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path("", views.home, name="home"),
    path('category/<slug:slug>/', views.category_products, name='category_products')
]