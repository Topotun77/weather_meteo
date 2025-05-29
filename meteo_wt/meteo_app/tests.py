from django.contrib.auth.models import User
from django.test import TestCase
from .models import Preferences, UserStat, CityStat
from django.urls import reverse
from .forms import CityForm


class UserStatTest(TestCase):
    def setUp(self):
        # создаем пользователя
        self.user = User.objects.create(username='testuser')

    def test_user_stat_creation(self):
        user_stat = UserStat.objects.create(user=self.user, city='Санкт-Петербург')
        self.assertEqual(str(user_stat.city), 'Санкт-Петербург')
        self.assertEqual(user_stat.user.username, 'testuser')
        # user_stat.delete()


class UserStatListTest(TestCase):
    """Тестирование представления user_stat_list."""

    @classmethod
    def setUpTestData(cls):
        # получаем пользователя
        cls.user = User.objects.create(username='testuser')
        # Создаем экземпляр UserStat
        cls.user_stat_1 = UserStat.objects.create(user=cls.user, city='Санкт-Петербург')

    def test_view_url_exists_at_desired_location(self):
        """Представление доступно по заданному адресу."""
        resp = self.client.get(reverse('meteo_app:user_stat_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """Правильный шаблон рендерится представлением."""
        resp = self.client.get(reverse('meteo_app:user_stat_list'))
        self.assertTemplateUsed(resp, 'user_statistic_list.html')

    def test_context_contains_user_stats(self):
        """Контекст содержит объекты UserStat."""
        resp = self.client.get(reverse('meteo_app:user_stat_list'))
        self.assertTrue('user_stat' in resp.context)
        self.assertIn(self.user_stat_1, resp.context['user_stat'])

    def test_empty_queryset(self):
        """Отображение работает правильно даже при отсутствии данных."""
        UserStat.objects.all().delete()
        resp = self.client.get(reverse('meteo_app:user_stat_list'))
        self.assertEqual(len(resp.context['user_stat']), 0)
        self.assertEqual(resp.status_code, 200)


class FormTests(TestCase):
    def test_form_is_valid(self):
        form_data = {'city': 'Москва'}
        form = CityForm('Москва', data=form_data)
        self.assertTrue(form.is_valid())
