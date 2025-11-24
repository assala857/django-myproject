from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_university),
    path('getAll/', views.get_all_universities),
]
