from .views import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("artikel/", artikel, name="artikel"),
    path("singleartikel/<int:id>", detailArtikel, name="detailArtikel"),
    path("about/", about, name="about"),
    path("weather/", cuaca, name="weather"),
    # apps
    path("dashboard/", include("blog.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)