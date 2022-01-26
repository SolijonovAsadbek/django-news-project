import logging

from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create trst your here
class PostModelsTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Mavzu", text="Yangi")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = post.title
        expected_object_text = post.text
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text, "Yangi")


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Mavzu 2", text="Yangi 2")

    def test_views_uls_exists_at_proper_location(self):
        resp = self.client.get('/')
        print("*" * 30, resp)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_name(self):
        resp = self.client.get(reverse('home'))
        print("*" * 30, self.client)
        print("*" * 30, resp)
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
