from django.db import models
from appUser.models import app_user

# Create your models here.

class education(models.Model):
    applicant = models.ForeignKey(app_user, on_delete=models.CASCADE,related_name='learn')

    course_qualification = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    finish_date = models.DateField()

    def __str__(self):
        return f"{self.course_qualification} at {self.institution}"
