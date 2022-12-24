from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib.auth.hashers import make_password
from .models import *

# Create your views here.
def is_direktur(user):
    if user.groups.filter(name="direktur").exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "back/dashboard.html"
    
    if request.user.groups.filter(name="direktur").exists():
        request.session['is_direktur'] = 'direktur'
    
    users = User.objects.all()
    
    context = {
        "users" : users
    }
    
    return render(request, template_name, context)

@login_required
def tableArtikel(request):
    template_name = "back/tableArtikel.html"
    
    view_artikel = MyArtikel.objects.filter(penulis=request.user)
    
    context ={
        "display" : view_artikel
    }
    
    return render(request, template_name, context)

@login_required
def tambahArtikel(request):
    template_name = "back/tambahArtikel.html"
    
    
    if request.method == "POST":
        myfile = request.FILES.get("gambarku")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        judul = request.POST.get("judul")
        konten = request.POST.get("konten1")
        gambar = url
        penulis = request.user
        
        MyArtikel.objects.create(
            penulis =penulis,
            Judul = judul,
            isiArtikel = konten,
            gambar = gambar,
        )
        return redirect(tableArtikel)
        
    
    return render(request, template_name)

@login_required
def editArtikel(request, id):
    template_name = "back/tambahArtikel.html"
    
    artikel_get = MyArtikel.objects.get(id=id)
    
    if request.method == "POST":
        myfile = request.FILES.get("gambarku")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        
        judul = request.POST.get("judul")
        konten = request.POST.get("konten1")
        gambar = url
        penulis = request.user
        
        artikel_get.penulis = penulis
        artikel_get.Judul = judul
        artikel_get.isiArtikel = konten
        artikel_get.gambar = gambar
        artikel_get.save()
        
        return redirect(tableArtikel)
    
    context ={
        "view" : artikel_get
    }
        
        
    
    return render(request, template_name, context)

@login_required
def hapusArtikel(request, id):
    MyArtikel.objects.get(id=id).delete()
    return redirect(tableArtikel)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    template_name = "back/login.html"
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request ,username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("username benar")
            return redirect('dashboard')
        else:
            print("username salah")
        
        
    
    return render (request, template_name)

@login_required
@user_passes_test(is_direktur)
def registerPage(request):
    template_name= "back/register.html"
    with transaction.atomic():
        if request.method == "POST":
            username = request.POST.get('username')
            get_password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            
            User.objects.create(
                username = username,
                password = make_password(get_password),
                first_name = first_name,
                last_name = last_name,
                email = email,
            )
            
            return redirect(dashboard)
            
    return render(request, template_name)

@login_required
@user_passes_test(is_direktur)
def editUser(request, id):
    template_name= "back/register.html"
    
    get_user = User.objects.get(id=id)
    
    with transaction.atomic():
        if request.method == "POST":
            username = request.POST.get('username')
            get_password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            
            get_user.username = username
            get_user.password = make_password(get_password)
            get_user.first_name = first_name
            get_user.last_name = last_name
            get_user.email = email
            get_user.save()
            
            return redirect(dashboard)
        
    context = {
        "users" : get_user
    }
            
    return render(request, template_name, context)
    
@login_required
@user_passes_test(is_direktur)
def hapusUsers(request, id):
    User.objects.get(id=id).delete()
    return redirect(dashboard)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('home')
    
  