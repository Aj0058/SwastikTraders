from django.test import TestCase

# Create your tests here.
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Subject',
    'This is a test message.',
    settings.EMAIL_HOST_USER,
    ['techstech@gmail.com'],
    fail_silently=False,
)
