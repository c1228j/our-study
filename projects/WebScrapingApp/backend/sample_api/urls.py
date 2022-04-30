from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'sample_api'
urlpatterns = [
    path('news/', views.NewsView.as_view(), name="news"),
]