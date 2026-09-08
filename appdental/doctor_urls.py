from django.urls import path
from . import doctor_views

urlpatterns = [
    path('doctor_dashboard/',doctor_views.doctor_dashboard,name='doctor_dashboard'),
    path('doctor_logout/',doctor_views.doctor_logout,name='doctor_logout'),
    path("doctor_profile/", doctor_views.doctor_profile, name="doctor_profile"),
    # path(
    #     "my_appointments/",
    #     doctor_views.my_appointments,
    #     name="doctor_my_appointments"
    # ),
    path("my_patients/", doctor_views.my_patients, name="my_patients"),
    path("doctor_logout/", doctor_views.doctor_logout, name="doctor_logout"),
    path('doctor_profile/',doctor_views.doctor_profile, name="doctor_profile"),
    path(
        "doctor_appointments/",
        doctor_views.doctor_appointments,
        name="doctor_my_appointments"
    ),

    path(
        "doctor_appointments/approve/<int:id>/",
        doctor_views.approve_appointment,
        name="approve_appointment"
    ),

    path(
        "doctor_appointments/reject/<int:id>/",
        doctor_views.reject_appointment,
        name="reject_appointment"
    ),
]