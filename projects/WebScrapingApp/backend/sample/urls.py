from django.urls import path

from . import views

app_name = 'sample'

urlpatterns = [
    path('', views.SampleView.as_view(), name='sample'),
]