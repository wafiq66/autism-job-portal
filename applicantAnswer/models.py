from django.db import models
from employerQuestion.models import employer_question
from jobApplication.models import job_application
# Create your models here.

class applicant_answer(models.Model):
    job_application = models.ForeignKey(job_application, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(employer_question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()

    def __str__(self):
        return f"Answer to Q{self.question.question_no} for Application #{self.job_application.id}"

