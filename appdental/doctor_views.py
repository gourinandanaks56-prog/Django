from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required




def doctor_dashboard(request):

    if not request.user.is_authenticated:
        return redirect("doctor_login")

    if request.user.user_type != "doctor":
        return redirect("doctor_login")

    return render(
        request,
        "doctor_dashboard.html"
    )

@login_required
def doctor_profile(request):

    doctor = Doctor.objects.get(user=request.user)

    return render(request, "doctor_profile.html", {
        "doctor": doctor
    })

# @login_required
# def my_appointments(request):
#
#     doctor = Doctor.objects.get(user=request.user)
#
#     appointments = Appointment.objects.filter(
#         doctor=doctor
#     )
#
#     return render(
#         request,
#         "my_appointments.html",
#         {"appointments": appointments}
#     )

@login_required
def my_patients(request):

    doctor = Doctor.objects.get(user=request.user)

    appointments = Appointment.objects.filter(doctor=doctor)

    return render(request, "my_patients.html", {
        "appointments": appointments
    })


@login_required
def feedback_list(request):

    if request.user.is_superuser or request.user.user_type == "doctor":

        feedbacks = Feedback.objects.all().order_by("-created_at")

        return render(
            request,
            "admin_feedback_list.html",
            {
                "feedbacks": feedbacks
            }
        )

    else:
        return redirect("patient_dashboard")

def doctor_logout(request):

    logout(request)

    return redirect("login")

@login_required
def doctor_profile(request):

    doctor = Doctor.objects.get(user=request.user)

    if request.method == "POST":

        form = DoctorProfileForm(
            request.POST,
            instance=doctor
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("doctor_profile")

    else:

        form = DoctorProfileForm(instance=doctor)

    return render(
        request,
        "doctor_profile.html",
        {
            "form": form
        }
    )

@login_required
def doctor_appointments(request):

    doctor = Doctor.objects.get(user=request.user)

    appointments = Appointment.objects.filter(
        doctor=doctor
    ).order_by(
        "-appointment_date",
        "-appointment_time"
    )

    return render(
        request,
        "my_appointments.html",
        {
            "appointments": appointments
        }
    )

@login_required
def approve_appointment(request, id):

    doctor = Doctor.objects.get(user=request.user)

    appointment = get_object_or_404(
        Appointment,
        id=id,
        doctor=doctor
    )

    appointment.status = "Approved"
    appointment.save()

    return redirect("home")

@login_required
def reject_appointment(request, id):

    doctor = Doctor.objects.get(user=request.user)

    appointment = get_object_or_404(
        Appointment,
        id=id,
        doctor=doctor
    )

    appointment.status = "Rejected"
    appointment.save()

    return redirect("home")