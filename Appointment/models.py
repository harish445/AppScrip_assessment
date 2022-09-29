from django.db import models
from Nurse.models import Nurse

# Create your models here.

class Appointment(models.Model):
    appoint = models.OneToOneField(Nurse, on_delete=models.CASCADE)
    is_appoint = models.BooleanField(default=False)

