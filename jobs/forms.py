from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from jobs.models import JobUser


# class SignUpForm(UserCreationForm):
#     linkedin_profile = forms.CharField(max_length=200, required=False, help_text='Optional.')
#     cv = forms.FileField( required=False, help_text='Optional.')
#
#     class Meta:
#         model = JobUser
#         fields = ('username', 'linkedin_profile', 'password1', 'password2', 'cv')
