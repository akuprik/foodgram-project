import os

from django.core.cache import cache
from django.test import TestCase, Client


class CommonTests(TestCase):
    def setUp(self):
        self.client = Client()    # не авторизованный клиент
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@tt.ru',
            password='1235678'
        )
        self.client_logined = Client()   # авторизованный (залогиненый) клиент
        self.client_logined.force_login(self.user)
        self.group = Group.objects.create(
            title='tstgroup',
            slug='tstgroup',
            description='description'
        )
        """
        cache.clear()


class TestStaticUrl(CommonTests):

    def test_index(self):
        """
        Проверяет правильный отклик на пустой запрос
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        """
        Проверяет на правильный отклик при если не найдено
        """
        response = self.client.get('test404')
        self.assertEqual(response.status_code, 404)
