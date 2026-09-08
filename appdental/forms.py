from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class AdminRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type',
            'password1',
            'password2'
        ]


class DoctorForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Doctor
        fields = [
            "name",
            "specialization",
            "email",
            "phone",
            "experience",
            "username",
            "password",
        ]

class PatientForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = [
            "name",
            "email",
            "phone",
            "age",
            "address",
            "username",
            "password",
        ]

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            "doctor",
            "appointment_date",
            "appointment_time",
        ]

        widgets = {
            "appointment_date": forms.DateInput(attrs={"type": "date"}),
            "appointment_time": forms.TimeInput(
                attrs={"type": "time"}
            ),
        }


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = "__all__"

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['message']

        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Write your feedback...',
                'rows': 5
            })
        }


class DoctorProfileForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            "name",
            "specialization",
            "email",
            "phone",
            "experience",
        ]