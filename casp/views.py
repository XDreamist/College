from django.shortcuts import render, redirect

from casp.forms import RegistrationForm
from casp.models import Registration


# Create your views here.

def homepage(request):
    return render(request, 'index.html')

#def registration(request):
 #   return render(request, 'registration.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'r_form': form})

def viewTeachers(request):
    teachers = Registration.objects.all()
    return render(request, 'viewteachers.html', {'teachers': teachers})