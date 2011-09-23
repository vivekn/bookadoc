from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bookadoc.app.forms import PatientRegistrationForm, DoctorRegistrationForm, DoctorSearchForm
from bookadoc.app.models import DoctorProfile

def register_patient(request):
    """
    Registers new patients
    """
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PatientRegistrationForm()
    
    template_data = {
        'form': form,
    }
    
    return render_to_response('registration/registration.html', template_data, context_instance=RequestContext(request))

def register_doctor(request):
    """
    Registers new doctors
    """
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DoctorRegistrationForm()
    
    template_data = {
        'form': form,
    }
    
    return render_to_response('registration/registration.html', template_data, context_instance=RequestContext(request))

def index(request, username=None):
    """
    Displays user profile. User may be patient or doctor.
    Doctor's profile may be viewed by anyone.
    Patient's profile may be viwed only by doctors.
    """
    pass

def search(request):
    """
    Searches for a doctor based on:
    Name, Specialization, Location.
    """
    if request.method == 'POST':
        form = DoctorSearchForm(request.POST)
        query = request.POST.get('submit', None)
        if query:
            qset = DoctorProfile.objects
            name = request.POST.get('name', None)
            specialization = request.POST.get('specialization', None)
            location = request.POST.get('location', None)
            
            if name:
                qset = qset.filter(name__icontains=name)
            if specialization:
                qset = qset.filter(specialization__icontains=specialization)
            if location:
                qset = qset.filter(location__icontains=location)
            
            template_data = {
                'results': qset.all(),
            }
            
            return render_to_response('search.html', template_data, context_instance=RequestContext(request))
    else:
        form = DoctorSearchForm()
    
    template_data = {
        'form': form,
    }
    
    return render_to_response('search.html', template_data, context_instance=RequestContext(request))

def appointments_index(request, username=None):
    """
    Displays a list of appointments. User may be doctor or patient.
    """
    pass

def appointments_book(request, username=None):
    """
    Books an appointment. User may be patient or doctor.
    Doctors can use it to book slots in their schedules.
    """
    pass

def appointments_cancel(request, username=None):
    """
    Cancels an appointment, sending a message to the affected parties.
    Doctors can use it to cancel their already booked appointments.
    """
    pass
