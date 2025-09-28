from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GarbageReport
from .serializers import GarbageReportSerializer

@api_view(['GET'])
def get_reports(request):
    reports = GarbageReport.objects.all().order_by('-created_at')  # optional: latest first
    serializer = GarbageReportSerializer(reports, many=True)
    return Response(serializer.data)