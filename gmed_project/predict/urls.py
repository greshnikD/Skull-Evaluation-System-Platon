from django.urls import path

from . import views

urlpatterns = [
    path('save/', views.save_results),
    path('', views.recognize_image),
]
