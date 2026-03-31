""" custom form classes"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Company
User = get_user_model()
class SignUpFormRecruiter(UserCreationForm):
    """ custom sign up form"""
    # ROLES = [("")]
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company = forms.ModelChoiceField(queryset=Company.objects.all(),required=True)
    experience = forms.DecimalField(max_digits=3,decimal_places=1,required=True,min_value=0,help_text="Experience in years")
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2","company","experience"]

class SignUpFormApplicant(UserCreationForm):
    """ custom sign up form"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    resume = forms.FileField(required=True)
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2","resume"]

