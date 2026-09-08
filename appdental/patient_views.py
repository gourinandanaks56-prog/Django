from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def patient_register(request):

    if request.method == "POST":

        form = PatientForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, "patient_register.html", {"form": form})

            user = CustomUser.objects.create_user(
                username=username,
                password=form.cleaned_data["password"],
                user_type="patient"
            )

            Patient.objects.create(
                user=user,
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                age=form.cleaned_data["age"],
                address=form.cleaned_data["address"],
            )

            messages.success(request, "Patient Registered Successfully")

            return redirect("login")

    else:

        form = PatientForm()

    return render(request, "patient_register.html", {"form": form})




def patient_dashboard(request):

    return render(request, "patient_dashboard.html")


@login_required
def book_appointment(request):

    patient = Patient.objects.get(user=request.user)

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.status = "Pending"
            appointment.save()

            return redirect("patient_my_appointments")

        else:
            print("FORM ERRORS:", form.errors)

    else:
        form = AppointmentForm()

    return render(request, "book_appointment.html", {
        "form": form
    })


@login_required
def my_appointments(request):

    patient = Patient.objects.filter(
        user=request.user
    ).first()

    print("USER:", request.user)
    print("PATIENT:", patient)

    if patient:
        print("PATIENT ID:", patient.id)

        appointments = Appointment.objects.filter(
            patient=patient
        )

        print("COUNT:", appointments.count())

        for appointment in appointments:
            print(
                "APPOINTMENT:",
                appointment.id,
                appointment.patient,
                appointment.doctor,
                appointment.appointment_date,
                appointment.appointment_time,
                appointment.status
            )

    else:
        appointments = []

    return render(
        request,
        "my_appointments.html",
        {
            "appointments": appointments
        }
    )



def patient_logout(request):

    logout(request)

    return redirect("login")


@login_required
def give_feedback(request):

    patient = Patient.objects.get(user=request.user)

    if request.method == "POST":

        form = FeedbackForm(request.POST)

        if form.is_valid():

            feedback = form.save(commit=False)
            feedback.patient = patient
            feedback.save()

            messages.success(
                request,
                "Feedback submitted successfully."
            )

            return redirect("patient_dashboard")

    else:
        form = FeedbackForm()

    return render(
        request,
        "feedback_list.html",
        {"form": form}
    )