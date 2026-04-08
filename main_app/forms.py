""" custom form classes"""
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Application, Company, Job , Skill
User = get_user_model()
class SignUpFormRecruiter(UserCreationForm):
    """ custom sign up form"""
    # ROLES = [("")]
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company = forms.ModelChoiceField(queryset=Company.objects.all(),required=True)
    experience = forms.DecimalField(max_digits=3,decimal_places=1,required=True,min_value=0,help_text="Experience in years")

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match("^[a-zA-Z]+$", first_name):
            raise forms.ValidationError("First name should contain only letters")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match("^[a-zA-Z]+$", last_name):
            raise forms.ValidationError("Last name should contain only letters")
        return last_name

    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2","company","experience"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Sign up',css_class="btn btn-primary"))
        
    
class SignUpFormApplicant(UserCreationForm):
    """ custom sign up form"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    resume = forms.FileField(required=True)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),required=True)
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match("^[a-zA-Z]+$", first_name):
            raise forms.ValidationError("First name should contain only letters")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match("^[a-zA-Z]+$", last_name):
            raise forms.ValidationError("Last name should contain only letters")
        return last_name

    def clean_skills(self):
        if len(self.cleaned_data['skills']) > 5:
            raise forms.ValidationError("atmost 5 skills allowed to select")
        return self.cleaned_data['skills']
    
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2","resume","skills"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.enctype = 'multipart/form-data' # to handle file uploads
        self.helper.add_input(Submit('submit','Sign up',css_class="btn btn-primary"))

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Login',css_class="btn btn-primary"))

class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

    class Meta:
        model = Application 
        fields = ["cover_letter"]
    
class ChangeStatus(forms.Form):
    STATUS= [("PENDING","pending"),("REVIEWED","reviewed"),("REJECTED","rejected")]
    status = forms.ChoiceField()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["status"].choices = self.STATUS
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Update Status',css_class="btn btn-primary"))
    
class CreateJobForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Create Job',css_class="btn btn-primary"))
    class Meta:
        model = Job
        fields = ["title","description","location","deadline","salary_min","salary_max","job_type"]

class EditJobForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Update Job',css_class="btn btn-primary"))
    class Meta:
        model = Job
        fields = ["title","description","location","deadline","salary_min","salary_max","job_type"]