from django.urls import path
from . import views

urlpatterns = [
    path('backend_api/', views.submit_report, name='submit_report'),
]