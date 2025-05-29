from rest_framework import serializers
from meteo_app.models import CityStat


class CityStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityStat
        fields = '__all__'
