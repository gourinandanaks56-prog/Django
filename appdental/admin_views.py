from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from . models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def patient_list(request):
    patients = Patient.objects.all()

    return render(request, "patient_list.html", {
        "patients": patients
    })

def add_doctor(request):

    if request.method == "POST":

        form = DoctorForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Username already exists
            if CustomUser.objects.filter(username=username).exists():
                messages.error(
                    request,
                    "Username already exists. Please choose another username."
                )

                return render(
                    request,
                    "add_doctor.html",
                    {"form": form}
                )

            # Create login account
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                user_type="doctor"
            )

            # Create Doctor profile
            Doctor.objects.create(
                user=user,
                name=form.cleaned_data["name"],
                specialization=form.cleaned_data["specialization"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                experience=form.cleaned_data["experience"],
            )

            messages.success(
                request,
                "Doctor added successfully."
            )

            return redirect("doctor_list")

    else:
        form = DoctorForm()

    return render(
        request,
        "add_doctor.html",
        {"form": form}
    )
def doctor_list(request):

    doctors = Doctor.objects.all()

    return render(request, "doctor_list.html", {"doctors": doctors})

def appointment_list(request):

    appointments = Appointment.objects.all().order_by(
        "-appointment_date",
        "-appointment_time"
    )

    return render(
        request,
        "appointment_list.html",
        {
            "appointments": appointments
        }
    )


@login_required
def approve_appointment(request, id):

    appointment = Appointment.objects.get(id=id)

    appointment.status = "Approved"
    appointment.save()

    return redirect("appointment_list")


@login_required
def reject_appointment(request, id):

    appointment = Appointment.objects.get(id=id)

    appointment.status = "Rejected"
    appointment.save()

    return redirect("appointment_list")

def add_service(request):

    if request.method == "POST":

        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("service_list")

    else:
        form = ServiceForm()

    return render(request, "add_service.html", {"form": form})


def service_list(request):

    services = Service.objects.all()

    return render(request, "service_list.html", {"services": services})

def edit_service(request, id):

    service = get_object_or_404(Service, id=id)

    if request.method == "POST":

        form = ServiceForm(request.POST, instance=service)

        if form.is_valid():
            form.save()
            return redirect("service_list")

    else:
        form = ServiceForm(instance=service)

    return render(request, "add_service.html", {"form": form})


def delete_service(request, id):

    service = get_object_or_404(Service, id=id)
    service.delete()

    return redirect("service_list")

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


def delete_feedback(request, id):

    feedback = get_object_or_404(Feedback, id=id)
    feedback.delete()

    return redirect("feedback_list")

def reports(request):

    context = {

        "doctor_count": Doctor.objects.count(),

        "patient_count": Patient.objects.count(),

        "appointment_count": Appointment.objects.count(),

        "approved_count": Appointment.objects.filter(status="Approved").count(),

        "pending_count": Appointment.objects.filter(status="Pending").count(),

        "rejected_count": Appointment.objects.filter(status="Rejected").count(),

        "service_count": Service.objects.count(),

        "feedback_count": Feedback.objects.count(),

    }

    return render(request, "reports.html", context)


@login_required
def doctor_appointments(request):

    print("LOGIN USER:", request.user)
    print("USER ID:", request.user.id)

    try:
        doctor = request.user.doctor_profile
        print("DOCTOR:", doctor)
        print("DOCTOR ID:", doctor.id)

    except Exception as e:
        print("DOCTOR PROFILE ERROR:", e)
        return render(
            request,
            "doctor_appointments.html",
            {
                "appointments": [],
                "error": "Doctor profile not found."
            }
        )

    appointments = Appointment.objects.filter(
        doctor=doctor
    ).order_by(
        "-appointment_date",
        "-appointment_time"
    )

    print("APPOINTMENTS:", appointments)
    print("COUNT:", appointments.count())

    return render(
        request,
        "doctor_appointments.html",
        {
            "appointments": appointments
        }
    )

def admin_logout(request):

    logout(request)

    return redirect("login")