from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.TempIphoneView.as_view(), name ='index'),
]