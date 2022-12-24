from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class MyArtikel(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Judul = models.CharField(max_length=200) 
    isiArtikel = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    gambar = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.Judul, self.isiArtikel)
    
    class Meta:

        verbose_name_plural = 'MyArtikel'
        
class WeatherCek(models.Model):
    id_weather = models.IntegerField(blank=True, null=True)
    cuaca = models.CharField(max_length=225, blank=True, null=True)
    temp = models.CharField(max_length=225, blank=True, null=True)
    tmax = models.CharField(max_length=225, blank=True, null=True)
    tmin = models.CharField(max_length=225, blank=True, null=True)
    wind = models.CharField(max_length=225, blank=True, null=True)
    country = models.CharField(max_length=225, blank=True, null=True)
    symbol_country = models.CharField(max_length=225, blank=True, null=True)
    cloud = models.CharField(max_length=225, blank=True, null=True)
    lon = models.CharField(max_length=225, blank=True, null=True)
    lat = models.CharField(max_length=225, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.country, self.cuaca)
    
    class Meta:

        verbose_name_plural = 'MyWeather'