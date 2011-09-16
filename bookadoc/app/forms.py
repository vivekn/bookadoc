from django.contrib.auth.forms import UserCreationForm
from django import forms

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = PatientProfile
        fields = ('name', 'username', 'password1', 'password2', 'email', 'contact', 'gender')

class DoctorRegistrationForm(UserCreationForm):
    class Meta:
        model = DoctorProfile
        fields = ('name', 'username', 'password1', 'password2', 'email', 'contact', 'location',
                  'specialization', 'registration_id', 'gender')

class DoctorSearchForm(forms.Form):
    name = forms.CharField(max_length=50)
    specialization = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
