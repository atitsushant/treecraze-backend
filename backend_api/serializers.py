from rest_framework import serializers
from .models import GarbageReport

class GarbageReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarbageReport
        fields = '__all__'