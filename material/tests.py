from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from material.models import Course, Lesson, Subscription
from users.models import User


class TestLessons(APITestCase):
    """ Тестирование уроков """

    def setUp(self) -> None:
        self.user = User.objects.create(email="test77@example.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Test", description="Основы Test")
        self.lesson = Lesson.objects.create(
            course=self.course,
            title="Test Lesson",
            description="Test",
            owner=self.user,
            url_video="https://www.youtube.com/watch",
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """

        url = reverse("material:lesson_create")
        data = {
            "title": "Test Lesson",
            "description": "Test",
            "course": self.lesson.course.id,
            "url_video": "https://www.youtube.com/watch",
        }

        response = self.client.post(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(data.get("title"), "Test Lesson")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("url_video"), "https://www.youtube.com/watch")
        self.assertEqual(data.get("description"), "Test")

    def test_edit_lesson(self):
        """ Тестирование изменения урока """

        url = reverse("material:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Test Lesson",
            "description": "Test1",
            "course": self.lesson.course.id,
            "url_video": "https://www.youtube.com/watch1",
        }

        response = self.client.put(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)
        self.assertEqual(data.get("description"), "Test1")
        self.assertEqual(data.get("url_video"), "https://www.youtube.com/watch1")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)

    def test_read_lesson(self):
        """ Тестирование списка урока """

        url = reverse("material:lesson_list")

        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("count"), 1)

    def test_retrieve_lesson(self):
        """ Тестирование просмотра одного урока """

        url = reverse("material:lesson_get", args=(self.lesson.pk,))

        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)
        self.assertEqual(data.get("description"), "Test")
        self.assertEqual(data.get("url_video"), "https://www.youtube.com/watch")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)

    def test_delete_lesson(self):
        """ Тестирование удаления урока """

        url = reverse("material:lesson_delete", args=(self.lesson.pk,))
        data = {
            "title": "Test Lesson",
            "description": "Test",
            "course": self.lesson.course.id,
            "url_video": "https://www.youtube.com/watch",
        }

        response = self.client.delete(url, data=data)
        data = response.json()
        print(data)


class TestSubscription(APITestCase):
    """ Тестирование подписки """

    def setUp(self) -> None:
        self.user = User.objects.create(email="test77@example.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Python", description="Основы Python")
        self.url = reverse("material:subscription")

    def test_subscription_activate(self):
        """Тестирование активации подписки"""
        url = reverse('material:subscription-list')
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        print(temp_data)





    def test_subscribe_delete(self):
        Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('material:subscription-detail', args=(self.subscription.pk,))
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        print(temp_data)


