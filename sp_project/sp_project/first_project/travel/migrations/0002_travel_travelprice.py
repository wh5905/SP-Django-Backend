# Generated by Django 5.0.6 on 2024-06-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="travel",
            name="travelPrice",
            field=models.DecimalField(decimal_places=2, default="0.0", max_digits=10),
        ),
    ]
