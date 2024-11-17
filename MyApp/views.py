from django.shortcuts import render,redirect
from MyApp.models import Appointment

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'service-details.html')
def starter(request):
    return render(request, 'starter-page.html')
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'services.html')
def doctors(request):
    return render(request, 'doctors.html')
def department(request):
    return render(request, 'departments.html')
def appointments(request):
   if request.method == "POST":
       myappointment=Appointment(
                   name=request.POST['name'],
                   email=request.POST['email'],
                   phone=request.POST['phone'],
                   date=request.POST['date'],
                   doctor=request.POST['doctor'],
                   department=request.POST['department'],
                   message=request.POST['message'],
       )
       myappointment.save()
       return redirect('/show')
   else:
       return render(request,'appointments.html')
def show(request):
    allappointments= Appointment.objects.all()
    return render(request,'show.html',{'appointments':allappointments})
def delete(request, id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('show')
def edit(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.edit()
    return redirect('show')
def pay(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.pay()
    return redirect('show')


