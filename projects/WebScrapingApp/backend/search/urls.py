from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.ScrapingView.as_view(), name='index'),
    path('ukraine/', views.ScrapingUkraineView.as_view(), name='ukraine'),
]