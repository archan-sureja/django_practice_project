from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Company(models.Model):

    name = models.CharField(max_length=50)
    website = models.URLField(null=True,blank=True)
    description = models.TextField()
    created_at = models.DateField(default=timezone.localdate)

    def __str__(self):
        return f"{self.name}"

class Job(models.Model):

    JOB_TYPES = [("FULL","full-time"),("PART","part-time"),("CONTRACT","contract")]
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary_min =models.DecimalField(max_digits=7, decimal_places=2)
    salary_max = models.DecimalField(max_digits=8,decimal_places=2)
    location = models.CharField()
    job_type = models.CharField(choices=JOB_TYPES,default="FULL")
    is_active = models.BooleanField(default=True)
    posted_at = models.DateField(default=timezone.localdate)
    deadline = models.DateField(null=True,blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="jobs")

    def __str__(self):
        return f"{self.title} - {self.description}"

    def is_expired(self):
        if timezone.localdate() > self.deadline:
            return True
        return False
    
    class Meta:
        ordering = ["-posted_at"] #latest one at top 
        indexes = [ models.Index(fields=['-posted_at'])]

class User(AbstractUser):
    ROLES = [("REC","recruiter"),("APP","applicant")]
    role = models.CharField(choices=ROLES)
    # email = models.EmailField(unique=True)

class ApplicantProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="applicant_profile")
    resume = models.FileField(upload_to="resumes/")

    def __str__(self):
        return f"{self.user.get_full_name()}"

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="recruiter_profile")
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="recruiters")
    experience = models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return f"{self.user.get_full_name()}"

# signal to create profiles when user is created
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created and instance.role == "APP":
        ApplicantProfile.objects.create(user=instance)
    elif created and instance.role == "REC":
        RecruiterProfile.objects.create(user=instance)
    
    

    
class Application(models.Model):
    STATUS= [("PENDING","pending"),("REVIEWED","reviewed"),("REJECTED","rejected")]
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name="applications")
    applicant = models.ForeignKey(User,on_delete=models.CASCADE,related_name="applcations")
    cover_letter = models.FileField()
    status = models.CharField(choices=STATUS,default="PENDING")
    applied_at = models.DateField(default=timezone.localdate)

    def __str__(self):
        return f"{self.job} , status : {self.status}"

