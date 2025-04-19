from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def candidate_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_applicant and user.has_resume:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(request, "You must be a candidate and have a resume to access this page.")
            return redirect('dashboard')  # Replace 'dashboard' with your fallback URL name
    return _wrapped_view

def recruiter_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_recruiter and user.has_company:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(request, "You must be a recruiter and have a company to access this page.")
            return redirect('dashboard')  # Replace 'dashboard' with your fallback URL name
    return _wrapped_view
