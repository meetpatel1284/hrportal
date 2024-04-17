from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class HrRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','age','salary','dateofbirth','password1','password2']


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user .is_hr = True
        user .save()
        return user
    
class EmployeeRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','age','salary','dateofbirth','password1','password2']  


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user .is_employee = True 
        user .save()
        return user
    