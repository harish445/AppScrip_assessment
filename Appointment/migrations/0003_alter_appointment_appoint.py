# Generated by Django 4.1.1 on 2022-09-29 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nurse', '0001_initial'),
        ('Appointment', '0002_alter_appointment_appoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appoint',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Nurse.nurse'),
        ),
    ]