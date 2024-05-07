from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""

        self.about_content = About(
            title="About Me",
            content="This is about me.",
        )
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collboration form"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIsInstance(response.context["collaborate_form"], CollaborateForm)


def test_successful_collaboration_request_submission(self):
    """Test for a user requesting a collaboration"""
    self.client.login(username="myUsername", password="myPassword")
    post_data = {
        "name": "test name",
        "email": "test@email.com",
        "message": "test message",
    }
    response = self.client.post(reverse("about"))
    self.assertEqual(response.status_code, 200)
    self.assertIn(
        b"Collaboration request received! I endeavour to respond within 2 working days.",
        response.content,
    )
