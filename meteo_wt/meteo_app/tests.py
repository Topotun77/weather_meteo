from django.test import TestCase
from .models import Preferences, UserStat, CityStat
from django.urls import reverse
from .forms import CityForm


class UserStatTest(TestCase):
    def test_user_stat_creation(self):
        user_stat = UserStat(user=1, city='Санкт-Петербург')
        user_stat.save()
        self.assertEqual(user_stat.city, 'Санкт-Петербург')  # Проверяем сохранение заголовка
        self.assertEqual(user_stat.user, 1)  # Проверяем сохранение текста
        user_stat.delete()


# def home(request):
#     articles = Article.objects.all()
#     return render(request, 'home.html', {'articles': articles})


class HomePageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.article = Article.objects.create(title="Test Title", content="Test Content")

    def test_home_page_returns_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_articles_are_in_context(self):
        response = self.client.get(reverse('home'))
        self.assertIn(self.article, response.context['articles'])


class FormTests(TestCase):
    def test_form_is_valid(self):
        form_data = {'city': 'Москва'}
        form = CityForm(data=form_data)
        self.assertTrue(form.is_valid())