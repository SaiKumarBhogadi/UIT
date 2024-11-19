from django.db import models
from django.utils import timezone
# Create your models here.
from django.core.validators import RegexValidator

class CandidateRequirement(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    designation = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\d{10,13}$')]
    )
    company_name = models.CharField(max_length=100, verbose_name='Company Name')
    website = models.URLField(verbose_name='Website Link')
    email = models.EmailField(verbose_name='Contact Email')
    domain = models.CharField(max_length=100)
    experience = models.CharField(max_length=50, choices=[('Fresher', 'Fresher'), ('1-2 Years', '1-2 Years'), ('2-3 Years', '2-3 Years'), ('3-4 Years', '3-4 Years'), ('5+ Years', '5+ Years')])
    positions = models.IntegerField(verbose_name='No. of Vacancies:')
    salary = models.CharField(max_length=50, verbose_name='Package')
    location = models.CharField(max_length=300)
    job_description = models.FileField(upload_to='job_descriptions/', null=True, blank=True, verbose_name='Job Description')
    profile_pic = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Profile Picture')
    message = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date Added')  # Field to track object creation date

    def __str__(self):
        return f"{self.full_name} {self.designation} - {self.company_name} - {self.domain}"


class InternshipStudents(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    course = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Profile Picture')

    def __str__(self):
        return f"{self.full_name} - {self.course}"