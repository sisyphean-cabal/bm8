# Generated by Django 4.0 on 2021-12-17 04:58

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0004_remove_profile_albums_remove_profile_bands_and_more")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "email",
                    models.CharField(blank=True, max_length=200, null=True, unique=True),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None, unique=True
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="band", name="albums"),
        migrations.RemoveField(model_name="band", name="genres"),
        migrations.RemoveField(model_name="profile", name="biography"),
        migrations.RemoveField(model_name="profile", name="phone_number"),
        migrations.RemoveField(model_name="profile", name="soundcloud"),
        migrations.DeleteModel(name="Album"),
        migrations.DeleteModel(name="Band"),
        migrations.DeleteModel(name="Genre"),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("phone_number__isnull", False),
                    ("email__isnull", False),
                    _connector="OR",
                ),
                name="accounts_user_email_or_phone_number",
            ),
        ),
    ]
