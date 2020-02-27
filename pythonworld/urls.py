from django.urls import path
from . import views


urlpatterns = [
    path('', views.pythonworld, name='pythonworld'),
    path('courses/', views.courses, name='courses'),
]