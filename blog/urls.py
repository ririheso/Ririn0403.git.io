from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("tableartikel/", tableArtikel, name="tableartikel"),
    path("tambahartikel/", tambahArtikel, name="tambahartikel"),
    path("editartikel/<int:id>", editArtikel, name="editArtikel"),
    path("deleteartikel/<int:id>", hapusArtikel, name="deleteArtikel"),
    path("loginPage/", loginPage, name="login"),
    path("registerPage/", registerPage, name="register"),
    path("editUser/<int:id>", editUser, name="edituser"),
    path("hapusUser/<int:id>", hapusUsers, name="hapususer"),
    path("logout/", logoutPage, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)