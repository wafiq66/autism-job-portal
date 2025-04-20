from django.db import models
from appUser.models import app_user
from jobAd.models import job_ad

# Create your models here.

APPLICATION_STATUS_CHOICES = [
    ('pending', 'Pending'), #Wait to be reviewed by the employer
    ('waiting_for_interview', 'Waiting for Interview'), #set the interview date
    ('interviewed', 'Interviewed'), #done interviewed or any other process
    ('offered', 'Job Offered'), #employer send offer letter
    ('rejected', 'Rejected'), #employer reject applicant
    ('withdrawn', 'Withdrawn'), #applicant withdraw application (can do anytime)
    ('hired', 'Hired'), #applicant accepted the job offer
]

class job_application(models.Model):
    applicant = models.ForeignKey(app_user, on_delete=models.CASCADE, related_name='application')
    job = models.ForeignKey(job_ad, on_delete=models.CASCADE, related_name='application')

    job_status = models.CharField(
        max_length=255,
        choices=APPLICATION_STATUS_CHOICES,
        default='draft'  # Set default to Draft if no status is selected
    )

    application_date = models.DateField(auto_now_add=True)
    # ✅ New field for interview date (optional)
    interview_date = models.DateField(blank=True, null=True)
    # ✅ New field for offer letter date (optional)
    offer_letter_date = models.DateField(blank=True, null=True)
     # When the employer rejects the applicant (“Rejected”)
    rejection_date = models.DateField(blank=True, null=True)
    # When the applicant withdraws their application (“Withdrawn”)
    withdrawal_date = models.DateField(blank=True, null=True)
    # When the applicant accepts the offer and is hired (“Hired”)
    hired_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.job_title}"
