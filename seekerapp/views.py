from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationTypeForm,Recruiterregform,Seekeregform,LoginForm,seekerupform,recruiterupform,ApplicationForm
from .models import Seekermodel,Recruitermodel,Jobmodel,Application
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registrationview(request):
    sform = Seekeregform() # here we have intialized both form outside the poat method because if u see in the code the sform and rform are intialized inside the if else body or reg form which is post and reg form as else which willn get reg form even if it not post method but sform and rform dont have else body outside Post method that will render em when its not Post method unlike regform hence we intializzed  them outside first
    rform = Recruiterregform()
    if request.method == 'POST':
        regtyform = RegistrationTypeForm(request.POST)
        if regtyform.is_valid():
            utype = regtyform.cleaned_data['ustype']
            if utype == 'seek':
                sform = Seekeregform(request.POST,request.FILES)
                if sform.is_valid():
                    user = sform.save(commit=False)
                    user.set_password(sform.cleaned_data['password'])
                    user.save()
                    return redirect('login')
            elif utype == 'recruit':
                rform = Recruiterregform(request.POST,request.FILES)
                if rform.is_valid():
                    user = rform.save(commit=False)
                    user.set_password(rform.cleaned_data['password'])
                    user.save()
                    return redirect('login')
            else:
                sform = Seekeregform()
                rform = Recruiterregform()
        return render(request, 'registration.html', {'seform': sform, 'reform': rform, 'regform': regtyform})
    else:
        regtyform = RegistrationTypeForm()
    return render(request, 'registration.html', {'regform': regtyform})
# def registrationview(request):
    # sform = Seekeregform()
    # rform = Recruiterregform()
    
#     if request.method == 'POST':
#         regtyform = RegistrationTypeForm(request.POST)
#         if regtyform.is_valid():
#             utype = regtyform.cleaned_data['ustype']
#             if utype == 'seek':
#                 sform = Seekeregform(request.POST)
#                 if sform.is_valid():
#                     sform.save()
#                     return redirect('loginpg')
#             elif utype == 'recruit':
#                 rform = Recruiterregform(request.POST)
#                 if rform.is_valid():
#                     rform.save()
#                     return redirect('loginpg')
#         return render(request, 'registration.html', {'seform': sform, 'reform': rform, 'regform': regtyform})
#     else:
#         regtyform = RegistrationTypeForm()
#         return render(request, 'registration.html', {'regform': regtyform})

# def loginview(request):
#     if request.method=='POST':
#         lform=LoginForm(request.POST)
#         if lform.is_valid():
#             name=lform.cleaned_data['username']
#             paw=lform.cleaned_data['password']
#             person=authenticate(request,username=name,password=paw)
#             if person is not None:
#                 login(request,person)
#                 if person.usertype=='seeker':
#                     return redirect('dashboard',u=person.pk)
#                 elif person.usertype=='recruiter':
#                     return redirect ('recruitboard')
#             else:
#                 messages.error(request, 'Incorrect credentials')
#     else:
#         lform=LoginForm()
#     return render (request,'login.html',{'loform':lform})
def loginview(request):
    if request.method == 'POST':
        lform = LoginForm(request.POST)
        if lform.is_valid():
            name = lform.cleaned_data['username']
            paw = lform.cleaned_data['password']
            person = authenticate(request, username=name, password=paw)
            if person is not None:
                
                login(request, person)
                if person.usertype == 'seeker':
                    return redirect('dashboard', u=person.pk)
                elif person.usertype == 'recruiter':
                    return redirect('recruitboard',u=person.pk)
            else:
                
                messages.error(request, 'Incorrect credentials')
        
    else:
        lform = LoginForm()
    return render(request, 'login.html', {'loform': lform})

def dashview(request, u):
    # Fetch the seeker based on the pk provided in the URL
    seekm = get_object_or_404(Seekermodel, pk=u)
    if request.user.pk != u:
        messages.error(request, "You do not have permission to view this dashboard.")
        return redirect('some_view')  # Redirect to a safe page or the home page
    return render(request, 'dash.html', {'user_data': seekm})


# or 
#    user_data = Seekermodel.objects.get(username=request.user.username)
#     return render(request, 'dashboard.html', {'user_data': user_data})
# /Both approaches are valid, but they differ in how they retrieve user data:
# The first approach (get_object_or_404) directly retrieves the user data based on the provided primary key (u), assuming you have access to the primary key of the logged-in user.
# The second approach retrieves the logged-in user's data from the Seekermodel based on the username stored in the request.user object. This approach is more common when you want to retrieve data specific to the logged-in user without explicitly passing the primary key.
# The "username" on the left side (username) is
# related to the model's schema and represents a field in the database table.
# The "username" on the right side (request.user.username) is 
# related to the currently logged-in user's username obtained from the user 
# authentication system (request.user). This value is determined by the user's 
# credentials and cannot be directly changed in this context.

def supdate(request, u):
    supm = get_object_or_404(Seekermodel, pk=u)
    if request.method == 'POST':
        sformobj = seekerupform(request.POST, request.FILES, instance=supm)
        if sformobj.is_valid():
            user = sformobj.save(commit=False)
            password = sformobj.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            return redirect('dashboard', u=user.pk)
    else:
        sformobj = seekerupform(instance=supm)
    return render(request, 'supdate.html', {'sup': sformobj})


def recruitview(request, u):
    recruitm = get_object_or_404(Recruitermodel, pk=u)
    
    # Fetch applications for jobs posted by this recruiter
    applications = Application.objects.filter(job__recruiter=recruitm)
    
    return render(request, 'recruitb.html', {'user_data': recruitm, 'applications': applications})



def rupdate(request, u):
    rupm = get_object_or_404(Recruitermodel, pk=u)
    if request.method == 'POST':
        rformobj = recruiterupform(request.POST, instance=rupm)
        if rformobj.is_valid():
            user = rformobj.save(commit=False)
            user.save()
            return redirect('recruitboard', u=user.pk)
    else:
        rformobj = recruiterupform(instance=rupm)

    return render(request, 'rupdate.html', {'rup': rformobj})

    

def apply_for_job(request, job_id):
    job = get_object_or_404(Jobmodel, pk=job_id)
    seeker = get_object_or_404(Seekermodel, username=request.user.username)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.seeker = seeker  # This assigns the correct seeker
            application.resume = request.FILES.get('resume')  # Use the uploaded resume if needed
            application.save()
            return redirect('jobb')
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form, 'job': job})




                    
                
            
                    
            
