from django import forms
from .models import UserDetail,UserRelative,RelationType,Celebration, CelebrationParticipants,Leave,Attendance
 


class UserDetailCreationForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(UserDetailCreationForm, self).__init__(*args, **kwargs)
        self.fields['dateofbirth'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['dateofjoining'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['lastappraisaldate'].widget = forms.DateInput(attrs={'type': 'date'})
    

class UserRelativeCreationForm(forms.ModelForm):
    class Meta:
        model = UserRelative
        fields = '__all__'   

class RelationTypeCreationForm(forms.ModelForm):
    class Meta:
        model = RelationType
        fields = '__all__'            

class CelebrationCreationForm(forms.ModelForm):
    class Meta:
        model = Celebration
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super(CelebrationCreationForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})          

class CelebrationParticipantsCreationForm(forms.ModelForm):
    class Meta:
        model = CelebrationParticipants
        fields = '__all__'        

class LeaveCreationForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LeaveCreationForm, self).__init__(*args, **kwargs)
        self.fields['dates'].widget = forms.DateInput(attrs={'type': 'date'})    

class AttendanceCreationForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AttendanceCreationForm, self).__init__(*args, **kwargs)
        self.fields['Date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['Signin'].widget = forms.TimeInput(attrs={'type': 'time'})
        self.fields['Signout'].widget = forms.TimeInput(attrs={'type': 'time'})            
       
        
