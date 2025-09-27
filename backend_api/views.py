from .models import GarbageReport
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def submit_report(request):
    photo = request.FILES.get('photo')
    description = request.data.get('description')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')

    report = GarbageReport.objects.create(
        photo=photo,
        description=description,
        latitude=latitude,
        longitude=longitude,
    )

    return Response({'message': 'Report saved', 'id': report.id})