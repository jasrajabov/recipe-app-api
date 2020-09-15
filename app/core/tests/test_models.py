from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successfull"""
        email = 'sample@gmail.com'
        password = 'TestPassword123'
        user = get_user_model().objects.create_user(
                                        email=email,
                                        password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalization(self):
        """Testing emails are normalized"""
        email = 'jasurbek@MAIL.ru'
        password = 'Test12345'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_invalid_email_raises_error(self):
        """Testing invalid email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test1234!')

    def test_super_user_creation(self):
        user = get_user_model().objects.create_superuser('admin@gmail.com',
                                                         'Test12345!')

        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
