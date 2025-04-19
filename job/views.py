from django.shortcuts import render, redirect
from datetime import timedelta, date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.core.mail import send_mail
from . import form as fm 
from .models import Job, JobApplication, SavedJob
from resume.models import Resume
from core.decorator import candidate_required, recruiter_required
from payment.models import Wallet
from .filters import ApplicationsPerJobFilter, MySavedJobFilter, MyJobsFilter

User = get_user_model()

@login_required
@recruiter_required
def create_job(request):
    wallet = Wallet.objects.get(user=request.user)

    if not request.user.company.is_verified:
        messages.warning(request, 'Company verificaiton process is still ongoing')
        return redirect('dashboard')
    
    if wallet.balance < 1000:
        messages.warning(request, 'Cannot create job. You wallet balance is less than 1,000 NGN. Please topup wallet')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = fm.CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.company = request.user.company
            var.user = request.user
            var.is_verified = True
            today = date.today()
            var.expiry_date = today + timedelta(weeks=2)
            var.save()

            wallet.balance = wallet.balance - 1000
            wallet.save()
            
            messages.success(request, 'Job has been created and published for display')
            return redirect('create-job')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            print(form.errors)
            return redirect('create-job')
    else:
        form = fm.CreateJobForm()
        context = {'form':form}
    return render(request, 'job/create_job.html', context)

@login_required
@recruiter_required
def update_job(request, pk):
    job = Job.objects.get(pk=pk)

    if not job.company == request.user.company:
        messages.warning(request, 'You cannot update this job, as it was not created by you')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = fm.UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job information updated and saved to Database')
            return redirect('update-job', job.pk)
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('update-job', job.pk)
    else:
        form = fm.UpdateJobForm(instance=job)
        context = {'job':job, 'form':form}
    return render(request, 'job/update_job.html', context)

@login_required
@recruiter_required
def delete_job(request, pk):
    job = Job.objects.get(pk=pk)

    if not job.company == request.user.company:
        messages.warning(request, 'You cannot delete this job, as it was not created by you')
        return redirect('dashboard')

    job.delete()
    messages.success(request, 'Job has been deleted. This would also delete all job applications')
    return redirect('my-jobs')

@login_required
@recruiter_required
def my_jobs(request):
    jobs = Job.objects.filter(user=request.user).order_by('-date_created') # you can also filter by company 

    # apply filter
    jobs_filter = MyJobsFilter(request.GET, queryset=jobs)
    filtered_jobs = jobs_filter.qs

    # pagination
    paginator = Paginator(filtered_jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj, 'filter':jobs_filter}
    return render(request, 'job/my_jobs.html', context)

@login_required
@recruiter_required
def applications_per_job(request, pk):
    job = Job.objects.get(pk=pk)
    applications = job.jobapplication_set.all().order_by('applied_on')

    # apply filter
    applications_filter = ApplicationsPerJobFilter(request.GET, queryset=applications)
    filtered_applications = applications_filter.qs

    # pagination
    paginator = Paginator(filtered_applications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'job':job, 'applications':page_obj, 'filter':applications_filter}
    return render(request, 'job/application_per_job.html', context)

@login_required
@candidate_required
def apply_to_job(request, pk):

    job = Job.objects.get(pk=pk)
    resume = Resume.objects.get(user=request.user)

    if JobApplication.objects.filter(job=job, resume=resume).exists():
        messages.warning(request, 'You have already applied for this job')
        return redirect('job-details', job.pk)
    
    if job.has_expired():
        messages.warning(request, 'You cannot apply to this job, because it has expired')
        return redirect('job-details', job.pk)
    
    if job.is_disabled == 'True':
        messages.warning(request, 'No longer accepting applications')
        return redirect('job-details', job.pk)

    JobApplication.objects.create(job=job, resume=resume)

    send_mail(
        'JOB APPLICATION SUBMITTED', 
        f'Hi {request.user.first_name}, We have submitted your application and notified the recruiter. All the best!', 
        'noreply@email.com', 
        [request.user.email], 
        fail_silently=False
        )

    messages.success(request, 'Your application was successful and is being under review by the recruiter')
    return redirect('job-details', job.pk)

def job_details(request, pk):
    job = Job.objects.get(pk=pk)

    has_applied = None
    if request.user.is_authenticated and request.user.is_applicant and request.user.has_resume:
        resume = Resume.objects.get(user=request.user)
        has_applied = JobApplication.objects.filter(job=job, resume=resume).first()

    context = {'has_applied':has_applied, 'job':job}
    return render(request, 'job/job_details.html', context)

@login_required
@candidate_required
def save_job(request, pk):
    job = Job.objects.get(pk=pk)

    if SavedJob.objects.filter(job=job, user=request.user).exists():
        messages.warning(request, 'You have already saved this job')
        return redirect('job-details', job.pk)
    
    SavedJob.objects.create(job=job, user=request.user)
    messages.success(request, 'Job has been saved for reference')
    return redirect('job-details', job.pk)

@login_required
@candidate_required
def my_saved_jobs(request):
    jobs = SavedJob.objects.filter(user=request.user).order_by('-saved_on')

    # apply filter
    jobs_filter = MySavedJobFilter(request.GET, queryset=jobs)
    filtered_jobs = jobs_filter.qs

    # pagination
    paginator = Paginator(filtered_jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj, 'filter':jobs_filter}
    return render(request, 'job/my_saved_jobs.html', context)

@login_required
@candidate_required
def delete_job_application(request, pk):
    application = JobApplication.objects.get(pk=pk)

    if not application.resume.pk == request.user.resume.pk:
        messages.warning(request, 'You cannot delete this application, as you did not create it')
        return redirect('applications-per-resume')
    
    application.delete()
    messages.success(request, 'Application has been deleted from the database')
    return redirect('applications-per-resume')

@login_required
@candidate_required
def delete_saved_job(request, pk):
    saved_job = SavedJob.objects.get(pk=pk)

    if not saved_job.user == request.user:
        messages.warning(request, 'You cannot delete this saved job')
        return redirect('my-saved-jobs')
    
    saved_job.delete()
    messages.success(request, 'Saved job has been removed from list')
    return redirect('my-saved-jobs')
