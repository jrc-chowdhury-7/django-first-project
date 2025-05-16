from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),  # It's a good habit to name your path
]
