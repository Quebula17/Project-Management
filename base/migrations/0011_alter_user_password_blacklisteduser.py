# Generated by Django 4.2.4 on 2023-12-09 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_rename_user_id_user_id_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                default="pbkdf2_sha256$600000$VAvUnAMLMO0ZlBiAPRGPKM$GtoMvRuXAdqInPbfuDk0zJ0fYViEH699IXJ4k/+piM8=",
                max_length=128,
            ),
        ),
        migrations.CreateModel(
            name="BlacklistedUser",
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
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
