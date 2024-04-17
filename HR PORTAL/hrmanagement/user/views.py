from asyncio import Task
from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from .models import User
from .forms import HrRegistrationForm , EmployeeRegistrationForm
#import setting.py
from django.conf import settings
#send_mail is built-in function in django
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from employee.models import UserDetail
from employee.models import Celebration,Leave
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
# Create your views here.
class HrRegisterView(CreateView):
    template_name = 'user/hr_register.html'
    model = User
    form_class = HrRegistrationForm
    success_url = '/user/login/'

    
class EmployeeRegisterView(CreateView):
    template_name = 'user/employee_register.html'
    model = User
    form_class = EmployeeRegistrationForm
    success_url = '/user/login/'   


class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User

    def get_success_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_hr:
                return reverse_lazy('hr_dashboard')  # Redirect HR users to HR dashboard
            else:
                return reverse_lazy('employee_dashboard')  # Redirect non-HR employees to employee dashboard
        return reverse_lazy('login')  # Default redirection if user is not authenticated
    
    # def get_redirect_url(self):
    #    if self.request.user.is_authenticated:
    #       if self.request.user.is_hr:
    #             return '/user/hr_dashboard/'
    #       else:
    #             return '/user/employee_dashboard/'

def view_profile(request):
    user = request.user  # Get the current logged-in user
    # Add any additional logic to retrieve user profile data if needed
    return render(request, 'user_profile.html', {'user': user})
    
     
def logout_view(request):
    logout(request)
    return redirect("login")

        
class HrDashboardView(ListView):
    
   def get(self, request, *args, **kwargs):
       #logic to get all the projects
     userDetails = UserDetail.objects.all()
     leaves = Leave.objects.all()
     return render(request, 'user/hr_dashboard.html',{
         "userdetails":userDetails,
         "leaves":leaves
     })
    

   template_name = 'user/hr_dashboard.html'

class UpdateLeaveStatus(View):
    def post(self,request,pk):
        leave = Leave.objects.get(id=pk)

        if leave.status == "Pending":
            leave.status = "Approved"
        elif leave.status == "Approved":
            leave.status = "Rejected"
        else:
            leave.status = "Pending"

        leave.save()

        return redirect(reverse('hr_dashboard'))   

class EmployeeDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
      leaves = Leave.objects.all()
      print("leaves : ",leaves)
      return render(request, 'user/employee_dashboard.html',{
         "leaves":leaves
      })
        
    
    template_name = 'user/employee_dashboard.html'  


class UpdateTaskStatus(View):
    def post(self,request,pk):
        task = Leave.objects.get(id=pk)

        if task.status == "Pending":
            task.status = "Approved"
        elif task.status == "Approved":
            task.status = "Rejected"
        else:
            task.status = "Pending"

        task.save()

        return redirect(reverse('employee_dashboard'))