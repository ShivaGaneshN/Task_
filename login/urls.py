from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('signin/', include('frontend.urls')),
]