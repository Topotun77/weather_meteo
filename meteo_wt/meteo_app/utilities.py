import logging
import requests
from geopy.geocoders import Nominatim
from .models import CityStat


def get_coordinates(city_name: str) -> dict | None:
    """
    Получить координаты по названию города
    :param city_name: Название города
    :return: координаты - широта и долгота
    """
    try:
        geolocator = Nominatim(user_agent="weather-app")
        location = geolocator.geocode(city_name)

        return {
            "latitude": location.latitude,
            "longitude": location.longitude
        }
    except Exception as e:
        logging.error(f"Ошибка при получении координат: {e}")
        return None


def get_weather_forecast(latitude, longitude):
    """
    Получить прогноз погоды
    :param latitude: широта
    :param longitude: долгота
    :return: прогноз погоды или текст ошибки
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m"],
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "timezone": "auto",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "hourly" in data:
        times = data["hourly"]["time"][:24]
        temps = data["hourly"]["temperature_2m"][:24]
        hourly_data = zip(times, temps)

        times = data["daily"]["time"]
        temps_max = data["daily"]["temperature_2m_max"]
        temps_min = data["daily"]["temperature_2m_min"]
        daily_data = zip(times, temps_max, temps_min)

        return hourly_data, daily_data
    else:
        return "Ошибка при получении погодных данных."


def request_weather(city_name) -> list | str:
    """
    Выполнить запрос прогноза погоды
    :param city_name: Название города
    :return: прогноз погоды или текст ошибки
    """
    try:
        city = CityStat.object.get(city=city_name)
        if city.latitude or city.longitude:
            city.query_count += 1
            city.save()
            return get_weather_forecast(city.latitude, city.longitud)
    except BaseException:
        logging.info(f'Города {city_name} нет в базе')

    coordinates = get_coordinates(city_name)
    if not coordinates:
        return "Не удалось получить координаты города."

    lat = coordinates["latitude"]
    lon = coordinates["longitude"]
    try:
        city = CityStat.objects.get(city=city_name)
        city.query_count += 1
        city.latitude = lat
        city.longitude = lon
        city.save()
    except BaseException as er:
        CityStat.objects.create(city=city_name, latitude=lat, longitude=lon)
    return get_weather_forecast(lat, lon)
