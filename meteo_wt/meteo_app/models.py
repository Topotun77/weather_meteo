from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserStat(models.Model):
    """  Модель статистики по пользователям  """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, default='Санкт-Петербург')
    period = models.IntegerField(default=7)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'

    def __str__(self):
        return (f'Пользователь - {self.user}: '
                f'город - {self.city}, '
                f'период - {self.period}, '
                f'дата - {self.created_at}')


class CityStat(models.Model):
    city = models.CharField(max_length=255)
    query_count = models.IntegerField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Статистика по городам'
        verbose_name_plural = 'Статистика по городам'

    def __str__(self):
        return f'{self.city} - {self.query_count}'


class Preferences(models.Model):
    """  Модель таблицы пользовательских предпочтений  """
    themes = (
        ('light', 'Light Theme'),
        ('dark', 'Dark Theme'),
    )

    preference_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    theme = models.CharField(max_length=255, choices=themes, default='light')
    current_city = models.CharField(max_length=255, default='Санкт-Петербург')

    class Meta:
        verbose_name = 'Пользовательские предпочтения'
        verbose_name_plural = 'Пользовательские предпочтения'
        constraints = [
            models.UniqueConstraint(fields=['user'], name='Одна запись на пользователя')
        ]
    def __str__(self):
        return (f'Пользователь {self.user}: '
                f'тема - {self.theme}, '
                f'город - {self.current_city}')