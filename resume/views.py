from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from . import form as fm 
from .models import Resume
from core.decorator import candidate_required
from .filters import ApplicationsPerResumeFilter

User = get_user_model()

@login_required
def add_resume(request):

    if request.user.is_recruiter and request.user.has_resume:
        return redirect('update-resume', request.user.resume.pk)
    
    if request.method == 'POST':
        form = fm.AddResumeForm(request.POST, request.FILES)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            
            user = User.objects.get(pk=request.user.pk)
            user.has_resume = True
            user.save()

            messages.success(request, 'Your resume has been created. You can start applying for jobs now')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('add-resume')
    else:
        form = fm.AddResumeForm()
        context = {'form':form}
    return render(request, 'resume/add_resume.html', context)

@login_required
def update_resume(request, pk):
    resume = Resume.objects.get(pk=pk)

    if request.method == 'POST':
        form = fm.UpdateResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume information has been updated')
            return redirect('update-resume', resume.pk)
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('update-resume', resume.pk)
    else:
        form = fm.UpdateResumeForm(instance=resume)
        context = {'form':form}
    return render(request, 'resume/update_resume.html', context)

@login_required
def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume':resume}
    return render(request, 'resume/resume_details.html', context)

@login_required
@candidate_required
def applications_per_resume(request):
    resume = Resume.objects.get(user=request.user.pk)
    applications = resume.jobapplication_set.all().order_by('-applied_on')

    # apply filter
    applications_filter = ApplicationsPerResumeFilter(request.GET, queryset=applications)
    filtered_applications = applications_filter.qs

    # pagination
    paginator = Paginator(filtered_applications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'applications':page_obj, 'filter':applications_filter}
    return render(request, 'resume/applications_per_resume.html', context)