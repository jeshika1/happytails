from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from happytailsapp.forms import ContactMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from .models import AdoptionApplication, Animal, addyours,Process
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

@login_required(login_url='login/')
def page(request):
    animals = Animal.objects.all()
    return render(request, 'main/page.html', {'animals': animals})

def contact(request): 
    if request.method == 'POST':
        form = ContactMessage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("Contact form submitted successfully!"); window.location.href = "/page";</script>')
    else:
        form = ContactMessage()

    return render(request, 'main/contact.html', {'form' : form})

def about(request):
    return render(request, 'main/about.html')

def form(request):
    if request.method == 'POST':
       uname = request.POST.get('name')
       uaddress = request.POST.get('address')
       uphone = request.POST.get('phone')
       uemail = request.POST.get('email')
       uresident = request.POST.get('residenceType')
       uexcercisePlan = request.POST.get('exercisePlan')
       uhoursAlone = request.POST.get('hoursAlone')
       upreviousPets = request.POST.get('previousPets')

        # Create a new pet instance
       application = AdoptionApplication(
            name=uname,
            address=uaddress,
            phone=uphone,
            email=uemail,
            residenceType=uresident,
            exercisePlan= uexcercisePlan,
            hoursAlone=uhoursAlone,
            previousPets=upreviousPets
        )

        # Save the pet instance to the database
       application.save()     
    return render(request, 'main/form.html')

def description(request):
     return render(request, 'main/description.html')

def login_views(request):
   if request.method== 'POST':
      username= request.POST.get('username')
      pass1= request.POST.get('password')
      user= authenticate(request, username=username, password=pass1)
      if user is not None:
         login(request, user)
         return redirect('page')
      else:
         return HttpResponse('<script>alert("username or password is incorrect!!"); window.location.href = "/login";</script>')
   return render(request, 'main/login.html')

def signup(request):
     if request.method== 'POST':
         uname= request.POST.get('username')
         email= request.POST.get('email')
         pass1= request.POST.get('password')
         pass2= request.POST.get('password1')
         

         try:
          # Attempt to create a new user
           my_user = User.objects.create_user(username=uname, email=email, password=pass1)
           my_user.save()
           return redirect('login')
         except IntegrityError:
           return HttpResponse("Username already exists. Please choose a different username.")


     return render(request, 'main/signup.html')

@login_required(login_url="login/")
def addyour(request):
    if request.method == 'POST':
       pet_image = request.FILES.get('petImage')
       pet_name = request.POST.get('petName')
       pet_weight = request.POST.get('petWeight')
       pet_breed = request.POST.get('petBreed')
       vaccination_status = request.POST.get('vaccinationStatus', 'Unknown')

        # Create a new pet instance
       pet = addyours(
            petImage=pet_image,
            petName=pet_name,
            petWeight=pet_weight,
            petBreed=pet_breed,
            vaccinationStatus=vaccination_status
        )

        # Save the pet instance to the database
       pet.save()
       return HttpResponse('<script>alert(Thankyou for your kind help!!"); window.location.href = "/page";</script>')

    return render(request, 'main/addyour.html', {'form' : form})

def logout(request):
 return redirect('home')


def linear_search(request):
     search = request.GET.get('q')
     animals = Animal.objects.all()
     context = {
        "animal": None,
        "search": search,
    }
     if search:
        animals = animals.filter(
            Q(name__icontains=search)|Q(image__icontains=search)|Q(description__icontains=search)
		)
        paginator = Paginator(animals, 10)
        page = request.GET.get('page')
        animals = paginator.get_page(page)

        context = {
		"animal": animals,
		"search": search,
        }
     return render(request, 'main/linear_search.html', context)

def accept_process(request, process_id):
    process = get_object_or_404(Process, pk=process_id)

    if process.status == 'pending':
        process.status = 'accepted'
        process.save()
        messages.success(request, f'Order {process_id} has been accepted.')
    else:
        messages.warning(request, f'Order {process_id} is not pending and cannot be accepted.')

    return redirect('admin:happytailsapp_process_changelist')  # Redirect to the order change list page in the admin

def deny_process(request, process_id):
    process = get_object_or_404(Process, pk=process_id)

    if process.status == 'pending':
        process.status = 'denied'
        process.save()
        messages.success(request, f'Process {process_id} has been denied.')
    else:
        messages.warning(request, f'Process {process_id} is not pending and cannot be denied.')

    return redirect('admin:happytailsapp_process_changelist')  # Redirect to the order change list page in the admin

def processStatusView(request, process_id):
    order = get_object_or_404(Process, pk=process_id)
    return render(request, 'main/tracker.html' ,{'order': order})