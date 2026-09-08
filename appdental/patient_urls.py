from django.urls import path
from . import patient_views

urlpatterns = [

    path(
        "patient_register/",
        patient_views.patient_register,
        name="patient_register"
    ),


    path(
        "patient_dashboard/",
        patient_views.patient_dashboard,
        name="patient_dashboard"
    ),

    path("book_appointment/", patient_views.book_appointment, name="book_appointment"),
    path(
        "my_appointments/",
        patient_views.my_appointments,
        name="patient_my_appointments"
    ),

    path(
        "patient_logout/",
        patient_views.patient_logout,
        name="patient_logout"
    ),

    path(
            "give_feedback/",
            patient_views.give_feedback,
            name="give_feedback"
        ),

]