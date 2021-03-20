from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating a new user with an emaill address is successful"""
        email = "test@umich.edu"
        password = "123456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailized(self):
        """Test the email for a new user is normalized"""
        email = "mofd@UMICH.edu"
        user = get_user_model().objects.create_user(email, "test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no emial provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "mofd@umich.edu",
            "123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_superuser)  # is_superuser is part of PermissionMixin
