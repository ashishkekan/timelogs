# Generated by Django 4.2.23 on 2025-06-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("avg_calc", "0007_leave_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=10,
            ),
        ),
    ]
