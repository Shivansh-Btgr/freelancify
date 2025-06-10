from django.db import models
from django.conf import settings

class Post(models.Model) :
    EXPERIENCE_CHOICES = [
        ('entry', 'Entry Level (0-1 years)'),
        ('junior', 'Junior (1-3 years)'),
        ('mid', 'Mid Level (3-5 years)'),
        ('senior', 'Senior (5-8 years)'),
        ('lead', 'Lead (8+ years)'),
    ]
    EDUCATION_CHOICES = [
        ('highschool', 'High School'),
        ('associate', 'Associate Degree'),
        ('bachelor', 'Bachelor\'s Degree'),
        ('master', 'Master\'s Degree'),
        ('phd', 'PhD'),
    ]
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
    ]
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    role = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    ed_req =  models.CharField(
        max_length=20,
        choices=EDUCATION_CHOICES,
        blank=True,
        null=True,
        default = "highschool"
    )
    job_type = models.CharField(
        max_length=20, 
        choices=JOB_TYPE_CHOICES, 
        default='full_time'
    )
    experience_required = models.CharField(
        max_length=20, 
        choices=EXPERIENCE_CHOICES, 
        default='entry'
    )
    remote_allowed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.role


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    resume = models.FileField(
        upload_to='resumes/',
        help_text='Upload your resume (PDF, DOC, DOCX)'
    )
    additional_info = models.TextField(
        blank=True,
        null=True,
        help_text='Any additional information you want to share'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('applicant', 'post')  # Prevent duplicate applications
        ordering = ['-applied_at']  # Most recent first
    
    def __str__(self):
        return f"{self.applicant.username} - {self.post.role}"