'''
from .models import Client
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['nsu_id', 'designation', 'department','gender', 'date_of_birth', 'mobile_number',
                  'emergency_contact_number', 'monthly_income','marital_status', 'religion',
                  'present_address', 'permanent_address', 'income_sources','referred_by', 'cgpa']


'''