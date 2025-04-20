from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

AUTISM_SEVERITY_CHOICES = [
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ]

class app_user(AbstractUser):
    # Address-related
    stress_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    # Company-related (for employer accounts)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Applicant-related fields
    applicant_autism_severity = models.CharField(
        max_length=10,
        choices=AUTISM_SEVERITY_CHOICES,
        blank=True,
        null=True
    )
    is_verified_autism = models.BooleanField(default=False)
    applicant_auditory_score = models.FloatField(blank=True, null=True)
    applicant_visual_score = models.FloatField(blank=True, null=True)
    applicant_tactile_score = models.FloatField(blank=True, null=True)
    applicant_communication_score = models.FloatField(blank=True, null=True)
    is_applicant_assisted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
