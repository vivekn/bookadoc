from django.db import models
from django.contrib.auth.models import User, UserManager

class PatientProfile(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50)
    contact = models.BigIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    objects = UserManager()
    
    def __unicode__(self):
        return name

class DoctorProfile(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    location = models.TextField()
    contact = models.BigIntegerField()
    registration_id = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    objects = UserManager()
    
    def __unicode__(self):
        return name

class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorProfile)
    patient = models.ForeignKey(PatientProfile)
    time = models.DateTimeField()
    
    def __unicode__(self):
        return '%s - %s' % (self.doctor.name, self.time)
