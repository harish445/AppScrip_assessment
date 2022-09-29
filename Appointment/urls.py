from django.urls import path
from .views import CreateNurseAppointment, GetAppointNurse, AppointmentUpdate

urlpatterns = [
    path('create-appointment/', CreateNurseAppointment.as_view()),
    path('get-appointment/', GetAppointNurse.as_view()),
    path('update-appointment/<int:appoint_id>', AppointmentUpdate.as_view()),
]