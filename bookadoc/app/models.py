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
        return self.name

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class DoctorProfile(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50)
    qualifications = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    registration_id = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    clinics = models.ManyToManyField(Clinic)
    
    objects = UserManager()
    
    def __unicode__(self):
        return self.name

class ClinicTime(models.Model):
    doctor = models.ForeignKey(DoctorProfile)
    clinic = models.ForeignKey(Clinic)
    from_time = models.TimeField()
    till_time = models.TimeField()
    
    def __unicode__(self):
        return '%s - %s' % (self.doctor, self.clinic)

class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorProfile)
    patient = models.ForeignKey(PatientProfile)
    time = models.DateTimeField()
    clinic = models.ForeignKey(Clinic)
    
    def __unicode__(self):
        return '%s - %s' % (self.doctor.name, self.time)
