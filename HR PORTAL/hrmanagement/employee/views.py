from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .forms import UserDetailCreationForm,RelationTypeCreationForm,CelebrationCreationForm,LeaveCreationForm
from .models import UserDetail,UserRelative,CelebrationParticipants,Leave
from .forms import UserDetailCreationForm,UserRelativeCreationForm,CelebrationParticipantsCreationForm,AttendanceCreationForm
from .models import UserDetail,Celebration,RelationType,Attendance
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView 
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from user.models import User


# Create your views here.

class UserDetailCreationView(CreateView):
    template_name = 'employee/create.html'
    model = UserDetail
    form_class = UserDetailCreationForm
    success_url = '/employee/list/'
    
class UserDetailListView(ListView):
    template_name = 'employee/list.html'
    model = UserDetail
    context_object_name = 'userdetails'

class UserRelativeCreateView(CreateView):
    template_name = "employee/create_relative.html"
    model = UserRelative 
    form_class = UserRelativeCreationForm
    success_url = "/employee/list/"   

class RelationTypeCreateView(CreateView):
    template_name = "employee/create_relationtype.html"
    model = RelationType
    form_class = RelationTypeCreationForm
    success_url = "/employee/list/"

class UserDetailDeleteView(DeleteView):
    model = UserDetail
    template_name = "employee/employee_delete.html"    
    success_url = "/employee/list/"

class UserDetailDetailView(DetailView):
    model = UserDetail
    context_object_name = "userdetails"
    template_name = "employee/employee_detail.html"  

class UserDetailUpdateView(UpdateView):
    model = UserDetail
    form_class = UserDetailCreationForm
    template_name = "employee/employee_update.html" 
    success_url = "/employee/list/" 

class CelebrationCreationView(CreateView):
    template_name = "celebration/create.html"
    model = Celebration
    form_class = CelebrationCreationForm 
    success_url = "/employee/celebration_list/"  

class CelebrationListView(ListView):
    template_name = 'celebration/list.html'
    model = Celebration
    context_object_name = 'celebrations'

class CelebrationParticipantsCreateView(CreateView):
    template_name = "celebration/create_participants.html"  
    model = CelebrationParticipants
    form_class = CelebrationParticipantsCreationForm
    success_url = "/employee/celebration_list/"

class CelebrationDeleteView(DeleteView):
    model = Celebration
    template_name = "celebration/celebration_delete.html"
    success_url = "/employee/celebration_list/"

class CelebrationDetailView(DetailView):
    model = Celebration
    context_object_name = "celebrations"
    template_name = "celebration/celebration_detail.html"

class CelebrationUpdateView(UpdateView):
    model = Celebration
    form_class = CelebrationCreationForm
    template_name = "celebration/celebration_update.html"
    success_url = "/employee/celebration_list/"   

class LeaveCreateView(CreateView):
    template_name = "leave/create.html"
    model = Leave
    form_class = LeaveCreationForm
    success_url = "/employee/leave_list/"

    def form_valid(self, form):
        # Assign the currently logged-in user to the user field of the leave instance
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        user_id = self.request.user.id
        user = get_object_or_404(User, pk = user_id)
        initial['user'] = user
        return initial
     

class LeaveListView(ListView):
    template_name = "leave/list.html"
    model = Leave
    context_object_name = "leaves" 


class LeaveDeleteView(DeleteView):
    model = Leave
    template_name = "leave/leave_delete.html"
    success_url = "/employee/leave_list/"

class LeaveDetailView(DeleteView):
    model = Leave
    context_object_name = "leaves"
    template_name = "leave/leave_detail.html" 

class LeaveUpdateView(UpdateView):
    model = Leave
    form_class = LeaveCreationForm
    template_name = "leave/leave_update.html"
    success_url = "/employee/leave_list/" 

class UpdateStatusView(View):
    
    def post(self, request, pk):
        # Get the leave instance
        leave = Leave.objects.get(id=pk)
        
        # Update the leave status based on the form data
        if leave.status == 'Pending':
            leave.status = 'Approved'
        elif leave.status == 'Approved':
            leave.status = 'Rejected'
        else:
            leave.status = "Pending"
        
        # Save the updated leave status
        leave.save()
        
        return redirect(reverse('employee_dashboard'))    

class AttendanceCreateView(CreateView):
    template_name = "attendance/create.html"
    model = Attendance
    form_class = AttendanceCreationForm
    success_url = "/employee/attendance_list/"

class AttendanceListView(ListView):
    template_name = "attendance/list.html"
    model = Attendance 
    context_object_name = "attendances"                      

