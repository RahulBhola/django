from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_ethereum, name='fetch_ethereum'),
]
