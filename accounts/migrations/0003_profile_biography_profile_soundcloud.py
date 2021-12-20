# Generated by Django 4.0 on 2021-12-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0002_rename_band_profile_bands_and_more")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="biography",
            field=models.CharField(default="My biography", max_length=1500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="soundcloud",
            field=models.CharField(default="Link", max_length=280),
            preserve_default=False,
        ),
    ]
