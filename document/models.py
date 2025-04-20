from django.db import models
from appUser.models import app_user
from jobApplication.models import job_application

DOCUMENT_TYPES = [
        ('resume', 'Resume'),
        ('cover_letter', 'Cover Letter'),
        ('diagnose_letter', 'Diagnose Letter'),
        ('certificates', 'Certificates'),
        # Add more types as needed
    ]

# Create your models here.
class document(models.Model):
     # Relationships
    uploaded_by = models.ForeignKey(
        app_user,
        on_delete=models.CASCADE,
        related_name='upload'
    )
    sent_to_applications = models.ManyToManyField(
        job_application,
        related_name='attach',
        blank=True
    )

    document_name = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    document_path = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.document_name
