# Generated by Django 4.0 on 2021-12-10 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.RenameField(model_name="profile", old_name="band", new_name="bands"),
        migrations.RenameField(
            model_name="profile", old_name="user", new_name="user_obj"
        ),
    ]
