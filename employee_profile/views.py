from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from django.http import HttpResponse
from .forms import EmployeeProfileForm
import csv
from django.utils import timezone
from django.db import IntegrityError
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView, DetailView
from decouple import config
# Create your views here.
# all employee list


class EmployeeView(View):
    """
    View presented to applicant upon first visit to platform.
    """
    def get(self, request):
        context = {'form': EmployeeProfileForm}
        return render(request, 'applicant/index.html', context)

    def post(self, request):
        form = EmployeeProfileForm(request.POST)
        if form.is_valid():
            applicant = Employee()
            for key, value in form.cleaned_data.items():
                if value:
                    setattr(applicant, key, value)
            applicant.save()
            html_template = loader.get_template('applicant/application_received.html')
            html_body = render_to_string(
                'applicant/applicant_email.html',
                {
                    'full_name': f'{applicant.first_name} {applicant.last_name}',
                    'applicant_id': f"{config('APP_HOST', default='127.0.0.1')}:"
                                    f"{config('APP_HOST_PORT', default='8000')}/register/{applicant.id}",
                }
            )
            signup_email = EmailMultiAlternatives(
                subject='Internship application received.',
                from_email='internship@bou.or.ug',
                to=[applicant.email],
                body=f'Hey thanks for registering. Id is {applicant.id}',
            )
            signup_email.attach_alternative(html_body, "text/html")
            signup_email.send()
            return HttpResponse(html_template.render({'applicant': applicant}))
        context = {'form': form}
        return render(request, 'applicant/index.html', context)

class EmployeeList(LoginRequiredMixin, PermissionRequiredMixin, ListView, SuccessMessageMixin):
    """
    List of all employees for HR to view.
    """
    context_object_name = 'applicants_list'
    template_name = "employee_profile/employee_list.html"
    model = Employee
    permission_required = 'employee_profile.view_EmployeeList'

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()  # or whatever
        return context

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'employee_profile/details.html'

    def get_queryset(self):
        query = Employee.objects.all().select_related('employeeprofile')
        return query