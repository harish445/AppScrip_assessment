from django.urls import path
from . import views
from .views import CreateNurse, NurseUpdate

urlpatterns = [
    path('', views.getRoutes),
    path('create-nurse/', CreateNurse.as_view()),
    path('update-nurse/<int:nurse_id>', NurseUpdate.as_view()),
]