from django.db import models
from appUser.models import app_user

JOB_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

# Create your models here.
class job_ad(models.Model):
    #foreign key connected to table app_user
    publisher = models.ForeignKey(app_user, on_delete=models.CASCADE, related_name='publish')

    #Job description
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    job_location = models.CharField(max_length=255)
    job_min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    stress_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    branch = models.CharField(max_length=255)

    #type of job timing
    is_full_time = models.BooleanField(default=False)
    is_part_time = models.BooleanField(default=False)
    is_internship = models.BooleanField(default=False)

    #for job matching
    auditory_score = models.FloatField(blank=True, null=True)
    visual_score = models.FloatField(blank=True, null=True)
    tactile_score = models.FloatField(blank=True, null=True)
    communication_score = models.FloatField(blank=True, null=True)

    
    # Use choices for job_status
    job_status = models.CharField(
        max_length=10,
        choices=JOB_STATUS_CHOICES,
        default='draft'  # Set default to Draft if no status is selected
    )

    publish_status = models.CharField(max_length=50)  # e.g., 'draft', 'published'
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.job_title