from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('new/', views.note_new, name='note_new'),
]