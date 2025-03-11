from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vacancies/', views.post_list, name='post_list'),  # Ensure this name matches
    path('vacancy/<int:id>/', views.vacancy_detail, name='vacancy_detail'),
]