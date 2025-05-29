import logging
from django.http import JsonResponse
from rest_framework.viewsets import ReadOnlyModelViewSet
from meteo_app.models import CityStat
from stat_api_app.serializers import CityStatsSerializer


class CityStatsViewSet(ReadOnlyModelViewSet):
    queryset = CityStat.objects.all()
    serializer_class = CityStatsSerializer


def get_cities(request):
    cities = CityStat.objects.values_list('city', flat=True)
    logging.info('Запрос списка городов /api/stat_api_app/get-cities/')
    return JsonResponse(list(cities), safe=False)
