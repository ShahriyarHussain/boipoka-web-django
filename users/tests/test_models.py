from django.contrib.auth.models import User
from django.test import TestCase
from backend.users.models import *
# Create your tests here.


class UserTestCase(TestCase):
    def test_user(self):
        self.assertEquals(
            User.objects.count(),
            0
        )


class ProfileTestCase(TestCase):
    def test_user(self):
        self.assertEquals(
            Profile.objects.count(),
            0
        )


class ReportTestCase(TestCase):
    def test_user(self):
        self.assertEquals(
            Report.objects.count(),
            0
        )


class MessageTestCase(TestCase):
    def test_user(self):
        self.assertEquals(
            Message.objects.count(),
            0
        )


class ReviewTestCase(TestCase):
    def test_user(self):
        self.assertEquals(
            Review.objects.count(),
            0
        )
