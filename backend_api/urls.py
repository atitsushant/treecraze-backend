from django.urls import path
from .views import submit_report, get_reports

urlpatterns = [
    path('reports/', get_reports, name='get-reports'),
    path('submit/', submit_report, name='submit-report'),
    path('api/', include('yourapp.urls')),
]
