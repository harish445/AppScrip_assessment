# Generated by Django 4.1.1 on 2022-09-29 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nurse', '0001_initial'),
        ('Appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nurse.nurse'),
        ),
    ]
