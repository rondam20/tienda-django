from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path("productos/", views.product_list, name="product_list"),
    path("producto/<slug:slug>/", views.product_detail, name="product_detail"),
]
