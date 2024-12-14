from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('/time/', views.time_page, name='time_page'),
    path('/calc/', views.calc_page, name='calc_page'),
]