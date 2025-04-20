from django.db import models
from appUser.models import app_user
# Create your models here.

class skill(models.Model):
    applicant = models.ForeignKey(app_user, on_delete=models.CASCADE,related_name="has")

    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name

