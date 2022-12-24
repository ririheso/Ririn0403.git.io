# Generated by Django 4.1.3 on 2022-12-21 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_myartikel_penulis"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeatherCek",
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
                ("id_weather", models.CharField(blank=True, max_length=225, null=True)),
                ("temp", models.CharField(blank=True, max_length=225, null=True)),
                ("tmax", models.CharField(blank=True, max_length=225, null=True)),
                ("tmin", models.CharField(blank=True, max_length=225, null=True)),
                ("wind", models.CharField(blank=True, max_length=225, null=True)),
                ("country", models.CharField(blank=True, max_length=225, null=True)),
                (
                    "symbol_country",
                    models.CharField(blank=True, max_length=225, null=True),
                ),
                ("cloud", models.CharField(blank=True, max_length=225, null=True)),
                ("lon", models.CharField(blank=True, max_length=225, null=True)),
                ("lat", models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
    ]