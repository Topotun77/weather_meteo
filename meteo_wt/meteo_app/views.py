import logging

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import SignUpForm, CityForm
from .models import Preferences, UserStat
from .utilities import request_weather


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """
    Представление - Выход из системы (logout)
    :param request: HttpRequest - запрос пользователя
    :return: HttpResponseRedirect - перенаправление на домашнюю страницу
    """
    logout(request)
    return redirect('login')


def home(request: HttpRequest):
    """
    Представление - Регистрация пользователя.
    :param request: HttpRequest - запрос пользователя.
    :return: После регистрации перенаправление на страницу с объявлениями.
    """
    return render(request, 'home.html')


def signup(request: HttpRequest):
    """
    Представление - Регистрация пользователя
    :param request: HttpRequest - запрос пользователя
    :return: После регистрации перенаправление на страницу с объявлениями
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            logging.info(f'Создан пользователь: {user}')
            login(request, user)
            return redirect('/meteo')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def meteo_request(request: HttpRequest):
    """
    Представление - Просмотр прогноза погоды.
    :param request: HttpRequest - запрос пользователя.
    :return: Остаемся на странице.
    """
    try:
        pref = Preferences.objects.get(user=request.user)
    except BaseException as er:
        logging.error(f'user_settings: {er}')
        Preferences.objects.create(user=request.user)
        pref = Preferences.objects.get(user=request.user)
    if request.method == 'POST':
        city = request.POST['city']
        if not city:
            city = 'Санкт-Петербург'
        form = CityForm(city, request.POST)
        if form.is_valid():
            logging.info(f'Запрос пользователя {request.user}: {city}')
            weather = request_weather(city)
            if type(weather) == str:
                return render(request, 'meteo_request.html',
                              {'form': form, 'error': weather})
            else:
                pref.current_city = city
                pref.save()
                stat = form.save(commit=False)
                stat.user = request.user
                stat.city = city
                stat.save()
                return render(request, 'meteo_request.html',
                              {
                                  'form': form,
                                  'hourly_data': weather[0],
                                  'daily_data': weather[1],
                                  'city': city
                              })
    else:
        form = CityForm(pref.current_city)
    return render(request, 'meteo_request.html', {'form': form})


def user_stat_list(request: HttpRequest):
    """
    Представление - Просмотр статистики по пользователям.
    :param request: HttpRequest - запрос пользователя.
    :return: Остаемся на странице.
    """
    user_stat = UserStat.objects.all()
    return render(request, 'user_statistic_list.html', {'user_stat': user_stat})
