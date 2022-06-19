from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('visor/', views.visor_page, name='visor'),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
