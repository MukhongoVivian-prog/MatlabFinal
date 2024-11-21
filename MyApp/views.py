from django.shortcuts import render,redirect

from MyApp.forms import AppointmentForm
from MyApp.models import Appointment, Contact,Member

# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password= request.POST['password'],
        ).exists():
            members =Member.objects.get(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            return render(request, 'index.html',{'members':members})
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')


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
def contact(request):
    if request.method == "POST":
        mycontacts = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontacts.save()
        return redirect('/contacts')
    else:
        return render(request,'contact.html')
def show(request):
    allappointments= Appointment.objects.all()
    return render(request,'show.html',{'appointments':allappointments})
def delete(request, id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def edit(request,id):
     editappointment=Appointment.objects.get(id=id)
     return render(request,'edit.html',{'appointment':editappointment})
def update(request,id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')
def register(request):
    if request.method ==   "POST":
        memberinfo=Member(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        memberinfo.save()
        return redirect('/login')
    else:
      return render(request,'register.html')
def login(request):
    return render(request,'login.html')