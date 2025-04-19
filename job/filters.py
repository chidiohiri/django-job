import django_filters
from job.models import JobApplication, SavedJob, Job

class ApplicationsPerJobFilter(django_filters.FilterSet):
    resume__first_name = django_filters.CharFilter(lookup_expr='icontains')
    resume__surname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = JobApplication
        fields = ['resume__first_name', 'resume__surname']

class MySavedJobFilter(django_filters.FilterSet): 
    job__title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = SavedJob
        fields = ['job__title']

class MyJobsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title']