from django.shortcuts import render
from job.models import Job
from .filters import JobFilter
from django.core.paginator import Paginator

def home(request):
    jobs = Job.objects.filter(is_disabled='False').order_by('-date_created')

    # apply filter
    jobs_filter = JobFilter(request.GET, queryset=jobs)
    filtered_jobs = jobs_filter.qs

    # pagination
    paginator = Paginator(filtered_jobs, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'jobs':page_obj, 'filter':jobs_filter}
    return render(request, 'website/home.html', context)