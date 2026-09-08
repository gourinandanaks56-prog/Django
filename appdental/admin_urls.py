from django.urls import path
from . import admin_views


urlpatterns = [
    path('', admin_views.home, name='home'),
    path('admin_dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('patients/', admin_views.patient_list, name='patient_list'),
    path('add_doctor/', admin_views.add_doctor, name='add_doctor'),
    path('doctor_list/', admin_views.doctor_list, name='doctor_list'),
    path('appointments/', admin_views.appointment_list, name='appointment_list'),
    path('approve_appointment/<int:id>/', admin_views.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', admin_views.reject_appointment, name='reject_appointment'),
    path('add_service/', admin_views.add_service, name='add_service'),
    path('service_list/', admin_views.service_list, name='service_list'),
    path('edit_service/<int:id>/', admin_views.edit_service, name='edit_service'),
    path('delete_service/<int:id>/', admin_views.delete_service, name='delete_service'),
    path('feedback/', admin_views.feedback_list, name='feedback_list'),
    path('delete_feedback/<int:id>/', admin_views.delete_feedback, name='delete_feedback'),
    path('reports/', admin_views.reports, name='reports'),
    path("doctor_appointments/",admin_views.doctor_appointments,name="doctor_appointments"),
    path('logout/', admin_views.admin_logout, name='logout'),
]