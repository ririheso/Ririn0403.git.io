from django.contrib import admin
from .models import *
# Register your models here.

class AdminArtikel(admin.ModelAdmin):
    list_display = ["penulis","judul", "konten", "date", "gambar"]

admin.site.register(MyArtikel)

class AdminWeather(admin.ModelAdmin):
    list_display = ["id","cuaca","temp", "tmax", "tmin", "wind","country", "symbol_country", "cloud", "lon", "lat"]

admin.site.register(WeatherCek, AdminWeather)