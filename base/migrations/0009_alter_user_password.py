# Generated by Django 4.2.4 on 2023-11-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                default="!DW7cQXjjg3KBnTqQYygGJzpERRJLc5ZsTe5XCssK", max_length=128
            ),
        ),
    ]