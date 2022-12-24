from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import requests
from blog.models import *

def home(request):
    template_name = 'front/home.html'
    
    URL1 = "https://api.openweathermap.org/data/2.5/weather?q=balikpapan&APPID=0574b7a690872fa41a25b9b70eb6d821&units=metric"
    
    a = requests.get(url = URL1)
    
    balikpapan = a.json()
    
    URL2 = "https://api.openweathermap.org/data/2.5/weather?q=bontang&APPID=0574b7a690872fa41a25b9b70eb6d821&units=metric"
    
    b = requests.get(url = URL2)
    
    bontang = b.json()
    
    URL3 = "https://api.openweathermap.org/data/2.5/weather?q=penajam&APPID=0574b7a690872fa41a25b9b70eb6d821&units=metric"
    
    c = requests.get(url = URL3)
    
    penajam = c.json()
    
    URL4 = "https://api.openweathermap.org/data/2.5/weather?q=samarinda&APPID=0574b7a690872fa41a25b9b70eb6d821&units=metric"
    
    d = requests.get(url = URL4)
    
    samarinda = d.json()
    
    URL5 = "https://api.openweathermap.org/data/2.5/weather?q=sendawar&APPID=0574b7a690872fa41a25b9b70eb6d821&units=metric"
    
    e = requests.get(url = URL5)
    
    sendawar = e.json()
    
    URL6 = "https://api.openweathermap.org/data/2.5/weather?q=tenggarong&APPID=0574b7a690872fa41a25b9b70eb6d821&units=metric"
    
    f = requests.get(url = URL6)
    
    tenggarong = f.json()
    
    
    
    
 
    
    context ={
        
        "kota1" : balikpapan,
        "weather1": balikpapan['weather'][0]['main'],
        "temp1" : balikpapan['main']['temp'],
        'tmax1' : balikpapan['main']['temp_max'],
        'tmin1' : balikpapan['main']['temp_min'],
        "kota2" : bontang,
        "weather2": bontang['weather'][0]['main'],
        "temp2" : bontang['main']['temp'],
        'tmax2' : bontang['main']['temp_max'],
        'tmin2' : bontang['main']['temp_min'],
        "kota3" : penajam,
        "weather3": penajam['weather'][0]['main'],
        "temp3" : penajam['main']['temp'],
        'tmax3' : penajam['main']['temp_max'],
        'tmin3' : penajam['main']['temp_min'],
        "kota4" : samarinda,
        "weather4": samarinda['weather'][0]['main'],
        "temp4" : samarinda['main']['temp'],
        'tmax4' : samarinda['main']['temp_max'],
        'tmin4' : samarinda['main']['temp_min'],
        "kota5" : sendawar,
        "weather5": sendawar['weather'][0]['main'],
        "temp5" : sendawar['main']['temp'],
        'tmax5' : sendawar['main']['temp_max'],
        'tmin5' : sendawar['main']['temp_min'],
        "kota6" : tenggarong,
        "weather6": tenggarong['weather'][0]['main'],
        "temp6" : tenggarong['main']['temp'],
        'tmax6' : tenggarong['main']['temp_max'],
        'tmin6' : tenggarong['main']['temp_min'],
    }
    
    return render(request, template_name, context)

def artikel(request):
    template_name = "front/artikel.html"
    
    artikels = MyArtikel.objects.all()
    
    context ={
        "info" : "Artikel",
        "artikelku" : artikels
    }
    
    return render(request, template_name, context)

def detailArtikel(request, id):
    template_name = "front/detailArtikel.html"
    
    artikels = MyArtikel.objects.get(id=id)
    
    context ={
        "info" : "Artikel",
        "artikelku" : artikels
    }
    
    return render(request, template_name, context)

def about(request):
    template_name = "front/about.html"
    
    context ={
        "info" : "About"
    }
    
    return render(request, template_name, context)

def cuaca(request):
    template_name = "front/cuaca.html"
    
    global wet
    wrt = request.POST.get("cuaca")
    
    URL = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID=0574b7a690872fa41a25b9b70eb6d821&units=metric".format(wrt)
    
    r = requests.get(url = URL)
    
    find = r.json() 
    if find['cod'] == 200:
        cek_wet = WeatherCek.objects.filter(country=find['name'])
        try:
            if cek_wet.exists():
                wet = cek_wet.first()
                wet.id_weather = find['weather'][0]['id']
                wet.cuaca = find['weather'][0]['main']
                wet.temp = find['main']['temp']
                wet.tmax = find['main']['temp_max']
                wet.tmin = find['main']['temp_min']
                wet.wind = find['wind']['speed']
                wet.country = find['name']
                wet.symbol_country= find['sys']['country']
                wet.cloud = find['clouds']['all']
                wet.lon = find['coord']['lon']
                wet.lat = find['coord']['lat']
                wet.save()
            else:
                WeatherCek.objects.create(
                    id_weather = find['weather'][0]['id'],
                    cuaca = find['weather'][0]['main'],
                    temp = find['main']['temp'],
                    tmax = find['main']['temp_max'],
                    tmin = find['main']['temp_min'],
                    wind = find['wind']['speed'],
                    country = find['name'],
                    symbol_country= find['sys']['country'],
                    cloud = find['clouds']['all'],
                    lon = find['coord']['lon'],
                    lat = find['coord']['lat'],
                    
                )
        except:
            if cek_wet.exists():
                wet = cek_wet.first()
                wet.id_weather = find['weather'][0]['id']
                wet.cuaca = find['weather'][0]['main']
                wet.temp = find['main']['temp']
                wet.tmax = find['main']['temp_max']
                wet.tmin = find['main']['temp_min']
                wet.wind = find['wind']['speed']
                wet.country = find['name']
                wet.cloud = find['clouds']['all']
                wet.lon = find['coord']['lon']
                wet.lat = find['coord']['lat']
                wet.save()
            else:
                WeatherCek.objects.create(
                    id_weather = find['weather'][0]['id'],
                    cuaca = find['weather'][0]['main'],
                    temp = find['main']['temp'],
                    tmax = find['main']['temp_max'],
                    tmin = find['main']['temp_min'],
                    wind = find['wind']['speed'],
                    country = find['name'],
                    cloud = find['clouds']['all'],
                    lon = find['coord']['lon'],
                    lat = find['coord']['lat'],
                    
                )
    else:
        return redirect(home)
            
    
    
    data2 = WeatherCek.objects.filter(country=find['name'])
    context = {
    "data" : data2,
    "info" : "Weather"
    }
    
    
    
    
    return render(request, template_name, context)

