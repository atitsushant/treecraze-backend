from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.submit_report, name='submit_report'),
]