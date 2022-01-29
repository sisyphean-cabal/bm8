# Generated by Django 4.0 on 2022-01-29 14:50

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_profile_user_obj"),
    ]

    operations = [
        migrations.CreateModel(
            name="AbsUserAccount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("email", models.EmailField(max_length=60, unique=True, verbose_name="email")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None, unique=True
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.AddConstraint(
            model_name="absuseraccount",
            constraint=models.CheckConstraint(
                check=models.Q(("phone_number__isnull", False), ("email__isnull", False), _connector="OR"),
                name="accounts_absuseraccount_email_or_phone_number",
            ),
        ),
    ]
