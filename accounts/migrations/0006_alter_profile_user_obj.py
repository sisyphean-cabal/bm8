# Generated by Django 4.0 on 2021-12-18 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_user_remove_band_albums_remove_band_genres_and_more")
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user_obj",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
            ),
        )
    ]