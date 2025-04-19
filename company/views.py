from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from . import form as fm 
from .models import Company
from core.decorator import recruiter_required

User = get_user_model()

@login_required
@recruiter_required
def add_company(request):
    
    if request.user.has_company:
        return redirect('update-company', request.user.company.pk)
    
    if request.method == 'POST':
        form = fm.AddCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            user = User.objects.get(pk=request.user.pk)
            user.has_company = True
            var.save()
            user.save()
            messages.success(request, 'Company information added. Please wait for 30 minutes so we can verify your company information')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            print(form.errors)
            return redirect('add-company')
    else:
        form = fm.AddCompanyForm()
        context = {'form':form}
    return render(request, 'company/add_company.html', context)

@login_required
@recruiter_required
def update_company(request, pk):
    company = Company.objects.get(pk=pk)

    if request.method == 'POST':
        form = fm.UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company information has been updated and saved to Database')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('update-company', company.pk)
    else:
        form = fm.UpdateCompanyForm(instance=company)
        context = {'form':form, 'company':company}
    return render(request, 'company/update_company.html', context)

@login_required
@recruiter_required
def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    jobs = company.job_set.all()
    context = {'company':company, 'jobs':jobs}
    return render(request, 'company/company_details.html', context)

def jobs_per_company(request, pk):
    company = Company.objects.get(pk=pk)
    jobs = company.job_set.all().order_by('-date_created')

    # paginator
    paginator = Paginator(jobs, 5)  # Show 7 notes per page
    page_number = request.GET.get('page')
    ticket_notes = paginator.get_page(page_number)

    context = {'company':company, 'jobs':ticket_notes,}
    return render(request, 'company/jobs_per_company.html', context)