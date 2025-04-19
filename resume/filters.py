import django_filters
from job.models import JobApplication

class ApplicationsPerResumeFilter(django_filters.FilterSet):
    job__title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = JobApplication
        fields = ['job__title']