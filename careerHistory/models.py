from django.db import models
from appUser.models import app_user
# Create your models here.

class career_history(models.Model):
    applicant = models.ForeignKey(app_user, on_delete=models.CASCADE,related_name="work")

    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    started_date = models.DateField()
    ended_date = models.DateField(null=True, blank=True)
    still_in_role = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
