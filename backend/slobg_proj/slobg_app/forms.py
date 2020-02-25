from .models import VolunteerRecord

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class DateInput(forms.DateInput):
    input_type = 'date'

class VolunteerRecordForm(forms.ModelForm):
    class Meta:
        model = VolunteerRecord
        fields = ('activity', 'hours', 'date', 'supervisor')
        widgets = {'date' : DateInput(attrs={'id':'dateTimePicker'})}

<<<<<<< HEAD
class FilterForm(forms.Form):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
=======

class FilterForm(forms.Form):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
>>>>>>> 258fe40924d2645afa4fce732d379f1e735629d0
