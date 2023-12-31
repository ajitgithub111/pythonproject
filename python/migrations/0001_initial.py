# Generated by Django 4.2.7 on 2023-11-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="pythonmodel",
            fields=[
                ("student_id", models.IntegerField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=15)),
                ("high_school_name", models.CharField(max_length=200)),
                ("graduation_year", models.IntegerField()),
                ("major", models.CharField(max_length=100)),
                ("is_admitted", models.BooleanField(default=False)),
                ("admission_date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
