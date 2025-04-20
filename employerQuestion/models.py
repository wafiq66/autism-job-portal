from django.db import models
from jobAd.models import job_ad
# Create your models here.

class employer_question(models.Model):
    job_ad = models.ForeignKey(job_ad, on_delete=models.CASCADE, related_name='question')
    question_no = models.IntegerField()
    question_ux_id = models.CharField(max_length=255)  # this looks like a unique question identifier

    def __str__(self):
        return f"Q{self.question_no} for {self.job_ad.job_title}"