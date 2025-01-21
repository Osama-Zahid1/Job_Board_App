from django.shortcuts import render,redirect,get_object_or_404
from .forms import Jobform
from seekerapp.models import Jobmodel,Recruitermodel


def jform(request, u):
    recruiter = get_object_or_404(Recruitermodel, pk=u)  # Get the recruiter based on the logged-in user

    if request.method == 'POST':
        form = Jobform(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = recruiter  # Automatically assign the recruiter
            job.save()
            return redirect('recruitboard', u=recruiter.pk)  # Redirect to the recruiter dashboard
    else:
        form = Jobform()

    return render(request, 'jform.html', {'jform': form, 'recruiter': recruiter})

        
def jobboard(request):
    jobj=Jobmodel.objects.all()
    return render(request,'jobboard.html',{'listing':jobj})



# Create your views here.
